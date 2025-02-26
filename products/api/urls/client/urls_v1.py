from django.urls import path, include
from ...views.client import views_v1 as views

app_name = "products"

client_products_urlpatterns = [
    path('', views.ClientProductsAPIView.as_view(), name='product-list'),
    path('create/', views.ProductCreateAPIView.as_view(), name='product-create')

]

urlpatterns = [path('client/', include(client_products_urlpatterns))]