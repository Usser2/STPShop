from rest_framework.serializers import ModelSerializer
from .models import PromoCode, UsedPromoCode


class PromoCodeSerializer(ModelSerializer):
    class Meta:
        model = PromoCode
        fields = ("id", "code", "description", "percent", "expiration_date")


class UsedPromoCodeSerializer(ModelSerializer):
    class Meta:
        model = UsedPromoCode
        fields = ("id", "user", "code")
