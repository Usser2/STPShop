from rest_framework import generics
from ..models import ProductImage
from ..serializers import ProductImageSerializer


class ProductImageCreateView(generics.CreateAPIView):
    queryset = ProductImage.objects.all()
    serializer_class = ProductImageSerializer
    lookup_field = 'id'


class ProductImageRetrieveView(generics.RetrieveAPIView):
    queryset = ProductImage.objects.all()
    serializer_class = ProductImageSerializer
    lookup_field = 'id'


class ProductImageUpdateView(generics.UpdateAPIView):
    queryset = ProductImage.objects.all()
    serializer_class = ProductImageSerializer
    lookup_field = 'id'


class ProductImageDeleteView(generics.DestroyAPIView):
    queryset = ProductImage.objects.all()
    serializer_class = ProductImageSerializer
    lookup_field = 'id'
