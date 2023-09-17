from rest_framework import generics
from ..models import OrderProduct
from ..serializers import OrderProductSerializer


class OrderProductCreateView(generics.CreateAPIView):
    queryset = OrderProduct.objects.all()
    serializer_class = OrderProductSerializer
    lookup_field = 'id'


class OrderProductRetrieveView(generics.RetrieveAPIView):
    queryset = OrderProduct.objects.all()
    serializer_class = OrderProductSerializer
    lookup_field = 'id'


class OrderProductUpdateView(generics.UpdateAPIView):
    queryset = OrderProduct.objects.all()
    serializer_class = OrderProductSerializer
    lookup_field = 'id'


class OrderProductDeleteView(generics.DestroyAPIView):
    queryset = OrderProduct.objects.all()
    serializer_class = OrderProductSerializer
    lookup_field = 'id'
