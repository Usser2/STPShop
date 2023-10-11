from django.shortcuts import render

from .tasks import promo_checker


def promo_checker_view(request):
    promo_checker(repeat=60)
