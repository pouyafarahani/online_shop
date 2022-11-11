from django.urls import path

from .views import ProductListView, ProductDetailView, ProductComment, test_view

urlpatterns = [
    path('', ProductListView.as_view(), name='product_list'),
    path('<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('comment/<int:product_id>/', ProductComment.as_view(), name='comment_create'),
    path('test/', test_view, name='test'),

]

