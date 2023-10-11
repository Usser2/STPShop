from django.db.models import Model, ForeignKey, BooleanField, CASCADE

from users.models import User
from . import PromoCode


class UserPromoCode(Model):
    user = ForeignKey(verbose_name="пользователь", to=User, on_delete=CASCADE)
    code = ForeignKey(verbose_name="промокод", to=PromoCode, on_delete=CASCADE)
    is_promo_used = BooleanField(verbose_name="использован ли промокод")

    class Meta:
        verbose_name = "использованный промокод"
        verbose_name_plural = "использованные промокоды"
