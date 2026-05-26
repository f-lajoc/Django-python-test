from django.urls import path
from product.views import Products, AddProduct, EditProduct, delete_product

urlpatterns = [ 
 path('products', Products.as_view(), name='products'),
 path('add-product', AddProduct.as_view(), name='add-product'),
 path('edit-product/<uuid:product_id>', EditProduct.as_view(), name='edit-product'),
 path('delete-product/<uuid:product_id>', delete_product, name='delete-product'),

]