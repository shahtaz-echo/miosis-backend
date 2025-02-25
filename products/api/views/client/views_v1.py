from rest_framework import generics
from django.shortcuts import get_object_or_404
from ...serializers import ProductViewSerializer
from products.models import Product

class ClientProductsAPIView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductViewSerializer
    