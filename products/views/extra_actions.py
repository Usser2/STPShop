from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.renderers import JSONRenderer

from ..serializers import ProductSerializer, SpecificationSerializer, ProductImageSerializer
from ..models import Product, ProductImage, Specification


class ProductViewSet(ViewSet):
    @action(detail=False, methods=['get'], url_path="by-category/<int:category_id>")
    def get_products_by_category_id(self, category_id):
        products = Product.objects.all().filter(category=category_id)
        serializer = ProductSerializer(products)

        return Response(JSONRenderer().render(serializer.data))


class SpecificationViewSet(ViewSet):
    @action(detail=False, methods=['get'], url_path="by-product/<int:product_id>")
    def get_specifications_by_product_id(self, product_id):
        specifications = Specification.objects.all().filter(product=product_id)
        serializer = SpecificationSerializer(specifications)

        return Response(JSONRenderer().render(serializer.data))


class ProductImageViewSet(ViewSet):
    @action(detail=False, methods=['get'], url_path="by-product/<int:product_id>")
    def get_images_by_product_id(self, product_id):
        images = ProductImage.objects.all().filter(product=product_id)
        serializer = ProductImageSerializer(images)

        return Response(JSONRenderer().render(serializer.data))
