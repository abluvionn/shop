from applications.product.models import Product
from rest_framework import serializers


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id','owner','description','price','category','images')
