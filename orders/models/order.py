from django.db.models import Model, ForeignKey, CASCADE, DecimalField, CharField, DateTimeField

from users.models import User


class Order(Model):
    user = ForeignKey(verbose_name="пользователь", to=User, on_delete=CASCADE)
    date = DateTimeField("дата заказа")
    status = CharField(max_length=100)
    address = CharField(max_length=200)
    total_price = DecimalField(max_digits=20, decimal_places=2)

    class Meta:
        verbose_name = "заказ"
        verbose_name_plural = "заказы"

    def __str__(self):
        return f"{self.user} - {self.status}"
