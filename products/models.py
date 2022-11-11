from django.db import models
from django.utils import timezone
from django.shortcuts import reverse
from django.contrib.auth import get_user_model
from django.utils.translation import gettext as _

from ckeditor.fields import RichTextField


class Product(models.Model):
    title = models.CharField(_('title'), max_length=100)
    description = RichTextField()
    shor_description = RichTextField(blank=True)
    price = models.PositiveIntegerField(_('price'), default=0)
    active = models.BooleanField(_('active'), default=True)
    image = models.ImageField(_('Image'), blank=True, upload_to='product/product_cover')

    datetime_create = models.DateTimeField(_('time product create'), default=timezone.now)
    datetime_edit = models.DateTimeField(_('time product edit'), auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('product_detail', args=[self.pk])


class comment(models.Model):
    PRODUCT_STARS = [
        ('1', 'very Bad'),
        ('2', 'Bad'),
        ('3', 'Normal'),
        ('4', 'Good'),
        ('5', 'very Good'),
    ]

    products = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='comments')

    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name=_('author comment'),
    )

    description = models.TextField(_('description comment'),)
    point = models.CharField(_('what is your point'), max_length=10, choices=PRODUCT_STARS)
    active = models.BooleanField(_('active'), default=True)

    datetime_create = models.DateTimeField(_('create comment'), auto_now_add=True)
    datetime_edit = models.DateTimeField(_('edit comment'), auto_now=True)
