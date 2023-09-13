from django.db.models import Model, ForeignKey, IntegerField, CASCADE

from products.models import Product
from . import Order


class OrderProduct(Model):
    order = ForeignKey(verbose_name="заказ", to=Order, on_delete=CASCADE)
    product = ForeignKey(verbose_name="товар", to=Product, on_delete=CASCADE)
    count = IntegerField(verbose_name="кол-во")

    class Meta:
        verbose_name = "заказ-товар"
        verbose_name_plural = "заказы-товары"
