from django.urls import path
from .views import get_products, create_product

user_urls = [
    path('get-products/', get_products, name='all-products')
]

admin_urls = [
    path('create-products/', create_product, name='create-products')
]

urlpatterns = user_urls + admin_urls