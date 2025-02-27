from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from ..serializers import ProductViewSerializer, ProductCreateSerializer
from ...models import Product

@api_view(['GET'])
def get_products(requests):
    products = Product.objects.all()
    serializer = ProductViewSerializer(products, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def create_product(request):
    print("------------------------")
    print(request.data)
    serializer = ProductCreateSerializer(data=request.data)
    
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status = status.HTTP_201_CREATED)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

