from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.renderers import JSONRenderer

from ..serializers import CartSerializer
from ..models import Cart


class CartViewSet(ViewSet):
    @action(detail=False, methods=['get'], url_path="by-user/<int:user_id>")
    def get_carts_by_user_id(self, user_id):
        orders = Cart.objects.all().filter(user=user_id)
        serializer = CartSerializer(orders)

        return Response(JSONRenderer().render(serializer.data))