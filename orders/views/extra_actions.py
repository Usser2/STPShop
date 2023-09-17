from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.renderers import JSONRenderer

from ..serializers import OrderSerializer, OrderProductSerializer
from ..models import Order, OrderProduct


class OrderViewSet(ViewSet):
    @action(detail=False, methods=['get'], url_path="by-user/<int:user_id>")
    def get_orders_by_user_id(self, user_id):
        orders = Order.objects.all().filter(user=user_id)
        serializer = OrderSerializer(orders)

        return Response(JSONRenderer().render(serializer.data))


class OrderProductViewSet(ViewSet):
    @action(detail=False, methods=['get'], url_path="by-order/<int:user_id>")
    def get_order_products_by_order_id(self, order_id):
        order_products = OrderProduct.objects.all().filter(order=order_id)
        serializer = OrderProductSerializer(order_products)

        return Response(JSONRenderer().render(serializer.data))
