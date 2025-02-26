from rest_framework import generics
from django.shortcuts import get_object_or_404
from ...serializers import ProductViewSerializer, ProductCreateSerializer
from products.models import Product

class ClientProductsAPIView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductViewSerializer


class ProductCreateAPIView(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductCreateSerializer
    