from background_task import background
from ..users.models import User
from ..cart.models import Cart
from models import PromoCode, UserPromoCode

from datetime import datetime, timedelta


@background(shedule=60)
def promo_checker():
    users = User.objects.all()
    for user in users:
        cart = Cart.get_full_user_cart(user)
        for item in cart:
            today = datetime.now().date()
            difference = item.saved_time - today
            if difference > timedelta(days=10):
                new_promo = PromoCode(user, str(user.name) + "10")
                new_promo.save()
                break
