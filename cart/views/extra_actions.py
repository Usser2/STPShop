from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.renderers import JSONRenderer

from ..serializers import CartSerializer
from ..models import Cart
from products.models import Product, Category
from products.serializers import ProductSerializer


class CartViewSet(ViewSet):
    @action(detail=False, methods=['get'], url_path="by-user/<int:user_id>")
    def get_carts_by_user_id(self, user_id):
        orders = Cart.objects.all().filter(user=user_id)
        cart_serializer = CartSerializer(orders)

        categories = [Category(Product(cart.product).category_id) for cart in orders]
        might_be_interesting = [Product.objects.all().filter(category_id__in=categories)]
        product_serializer = ProductSerializer(might_be_interesting)

        return Response(JSONRenderer().render(cart_serializer.data) + JSONRenderer().render(product_serializer.data))
