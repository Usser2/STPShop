from django.db.models import Model, ForeignKey, CASCADE

from users.models import User
from . import PromoCode


class UsedPromoCode(Model):
    user = ForeignKey(verbose_name="пользователь", to=User, on_delete=CASCADE)
    code = ForeignKey(verbose_name="промокод", to=PromoCode, on_delete=CASCADE)

    class Meta:
        verbose_name = "использованный промокод"
        verbose_name_plural = "использованные промокоды"
