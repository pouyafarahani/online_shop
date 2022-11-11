from django.contrib import admin
from .models import Product, comment
from jalali_date.admin import ModelAdminJalaliMixin


class CommentProduct(admin.TabularInline):
    model = comment
    fields = ['description', 'author', 'point', 'active', ]


@admin.register(Product)
class ProductAdmin(ModelAdminJalaliMixin, admin.ModelAdmin):
    list_display = ['title', 'price', 'active', ]
    inlines = [
        CommentProduct,
    ]


@admin.register(comment)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['author', 'point', 'active', ]
