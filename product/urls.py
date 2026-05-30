from django.urls import path
from product.views import Products, AddProduct, EditProduct, delete_product, list_products, buy_product

urlpatterns = [
    path('products/', Products.as_view(), name='products'),
    path('products/all/', list_products, name='all-prod'),
    path('add-product/', AddProduct.as_view(), name='add-product'),
    path('edit-product/<uuid:product_id>/', EditProduct.as_view(), name='edit-product'),
    path('buy-product/<uuid:product_id>/', buy_product, name='buy-product'),
    path('delete-product/<uuid:product_id>/', delete_product, name='delete-product'),
]