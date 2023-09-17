from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import *

cart_router = DefaultRouter()
cart_router.register('', CartViewSet, basename='cart-view-set')

cart_urlpatterns = [
    path('create/', CartCreateView.as_view(), name='order'),
    path('<int:id>/retrieve/', CartRetrieveView.as_view(), name='order'),
    path('<int:id>/update/', CartUpdateView.as_view(), name='order'),
    path('<int:id>/delete/', CartDeleteView.as_view(), name='order'),
] + cart_router.urls

