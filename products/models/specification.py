from django.db.models import Model, ForeignKey, CASCADE, CharField
from . import Product


class Specification(Model):
    product = ForeignKey(verbose_name="товар", to=Product, on_delete=CASCADE)
    name = CharField(verbose_name="характеристика", max_length=100)
    description = CharField(verbose_name="описание характеристики", max_length=100)

    class Meta:
        verbose_name = "характеристика"
        verbose_name_plural = "характеристики"
