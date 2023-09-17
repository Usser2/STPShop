from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import *

order_router = DefaultRouter()
order_router.register('', OrderViewSet, basename='order-view-set')

order_product_router = DefaultRouter()
order_product_router.register('', OrderProductViewSet, basename='order-product-view-set')

order_urlpatterns = [
    path('create/', OrderCreateView.as_view(), name='order'),
    path('<int:id>/update/', OrderRetrieveView.as_view(), name='order'),
    path('<int:id>/retrieve/', OrderUpdateView.as_view(), name='order'),
    path('<int:id>/delete/', OrderDeleteView.as_view(), name='order'),
] + order_router.urls

order_product_urlpatterns = [
    path('create/', OrderProductCreateView.as_view(), name='order-product'),
    path('<int:id>/update/', OrderProductRetrieveView.as_view(), name='order-product'),
    path('<int:id>/retrieve/', OrderProductUpdateView.as_view(), name='order-product'),
    path('<int:id>/delete/', OrderProductDeleteView.as_view(), name='order-product'),
] + order_product_router.urls
