from django.views import generic
from django.contrib import messages
from django.shortcuts import render, get_object_or_404, reverse

from .forms import CommentForm
from .models import Product, comment


class ProductListView(generic.ListView):
    queryset = Product.objects.filter(active=True)
    template_name = 'product/product_list.html'
    context_object_name = 'products'


class ProductDetailView(generic.DetailView):
    model = Product
    template_name = 'product/product_detail.html'
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment_form'] = CommentForm()
        return context


class ProductComment(generic.CreateView):
    model = comment
    form_class = CommentForm

    def get_success_url(self):
        return reverse('product_list')

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.author = self.request.user

        product_id = int(self.kwargs['product_id'])
        product = get_object_or_404(Product, id=product_id)
        obj.products = product

        return super().form_valid(form)


def test_view(request):
    messages.warning(request, 'salam chetori')
    messages.error(request, 'the error')

    return render(request, 'test.html')

