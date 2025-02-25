from rest_framework import serializers
from products.models import Product

class ProductViewSerializer(serializers.ModelSerializer):
    is_available = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ['id', 'title', 'description', 'price', 'stock', 'created_at', 'updated_at', 'is_available']
    
    def get_is_available(self, obj):
        return obj.stock>0