from django.db.models import (
    Model, CharField, TextField, ForeignKey,
    IntegerField, DecimalField, BooleanField, CASCADE
)

from . import Category


class Product(Model):
    name = CharField(verbose_name="наименование товара", max_length=100)
    description = TextField(verbose_name="описание товара")
    category_id = ForeignKey(
        verbose_name="категория",
        to=Category,
        to_field="id",
        on_delete=CASCADE
    )
    count = IntegerField(verbose_name="количество", default=1)
    price = DecimalField(verbose_name="цена", default=0, decimal_places=2, max_digits=15)
    is_for_sale = BooleanField(verbose_name="продается ли сейчас", default=False)

    class Meta:
        verbose_name = "товар"
        verbose_name_plural = "товары"

    def __str__(self):
        return self.name
