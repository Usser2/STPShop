from rest_framework.serializers import ModelSerializer
from .models import Category, Product, ProductImage, Specification


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ("id", "name")


class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = ("id", "name", "description", "category_id", "count", "price", "is_for_sale")


class ProductImageSerializer(ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ("id", "product", "cnt_number")


class SpecificationSerializer(ModelSerializer):
    class Meta:
        model = Specification
        fields = ("id", "product", "name", "description")
