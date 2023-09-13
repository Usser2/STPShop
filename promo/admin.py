from django.contrib import admin

from .models import PromoCode, UsedPromoCode


@admin.register(PromoCode)
class PromoCodeAdmin(admin.ModelAdmin):
    list_display = ["code", "percent", "expiration_date"]


@admin.register(UsedPromoCode)
class UsedPromoCodeAdmin(admin.ModelAdmin):
    list_display = ["user", "code"]
