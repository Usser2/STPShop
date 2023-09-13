from django.db.models import Model, ForeignKey, IntegerField, CASCADE

from products.models import Product
from users.models import User


class Cart(Model):
    user = ForeignKey(verbose_name="пользователь", to=User, on_delete=CASCADE)
    product = ForeignKey(verbose_name="товар", to=Product, on_delete=CASCADE)
    count = IntegerField(verbose_name="кол-во")

    class Meta:
        verbose_name = "пользователь-товар"
        verbose_name_plural = "пользователи-товары"
