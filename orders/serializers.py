from rest_framework.serializers import ModelSerializer
from .models import Order, OrderProduct


class OrderSerializer(ModelSerializer):
    class Meta:
        model = Order
        fields = ("id", "user", "date", "status", "address", "total_price")


class OrderProductSerializer(ModelSerializer):
    class Meta:
        model = OrderProduct
        fields = ("id", "order", "product", "count")
