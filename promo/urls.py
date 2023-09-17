from django.urls import path
from .views import *

promo_code_urlpatterns = [
    path('create/', PromoCreateView.as_view(), name='promo_code'),
    path('<int:id>/update/', PromoUpdateView.as_view(), name='promo_code'),
    path('<int:id>/retrieve/', PromoRetrieveView.as_view(), name='promo_code'),
    path('<int:id>/delete/', PromoDeleteView.as_view(), name='promo_code'),
]
used_promo_code_urlpatterns = [
    path('create/', UsedPromoCreateView.as_view(), name='used_promo_code'),
    path('<int:id>/update/', UsedPromoUpdateView.as_view(), name='used_promo_code'),
    path('<int:id>/retrieve/', UsedPromoRetrieveView.as_view(), name='used_promo_code'),
    path('<int:id>/delete/', UsedPromoDeleteView.as_view(), name='used_promo_code'),

]
