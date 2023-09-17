from django.contrib import admin
from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from users.urls import urlpatterns as user_urls
from promo.urls import promo_code_urlpatterns as promo_urls, used_promo_code_urlpatterns as used_promo_urls
from products.urls import (
    product_urlpatterns,
    product_image_urlpatterns,
    specification_urlpatterns,
    category_urlpatterns
)
from orders.urls import order_urlpatterns, order_product_urlpatterns

# from rest_framework import permissions


schema_view = get_schema_view(
    openapi.Info(
        title="API Documentation",
        default_version='v1',
        description="API Documentation",
        contact=openapi.Contact(email="contact@example.com"),
    ),
    public=True,
    # permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),

    # users
    path('api/users/', include(user_urls)),

    # promo
    path('api/promocode/', include(promo_urls)),
    path('api/used_promocode/', include(used_promo_urls)),

    # products
    path('api/product/', include(product_urlpatterns)),
    path('api/product-image/', include(product_image_urlpatterns)),
    path('api/specification/', include(specification_urlpatterns)),
    path('api/category/', include(category_urlpatterns)),

    # orders
    path('api/order/', include(order_urlpatterns)),
    path('api/order-product/', include(order_product_urlpatterns)),

    # swagger
    path('api-auth/', include('rest_framework.urls')),
    path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
