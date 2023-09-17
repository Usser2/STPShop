from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import *

product_router = DefaultRouter()
product_router.register('', ProductViewSet, basename='product-view-set')

image_product_router = DefaultRouter()
image_product_router.register('', ProductImageViewSet, basename='product-image-view-set')

spec_router = DefaultRouter()
spec_router.register('', SpecificationViewSet, basename='specification-view-set')


category_urlpatterns = [
    path('create/', CategoryCreateView.as_view(), name='category'),
    path('<int:id>/update/', CategoryUpdateView.as_view(), name='category'),
    path('<int:id>/retrieve/', CategoryRetrieveView.as_view(), name='category'),
    path('<int:id>/delete/', CategoryDeleteView.as_view(), name='category'),
]
product_urlpatterns = [
    path('create/', ProductCreateView.as_view(), name='product'),
    path('<int:id>/update/', ProductUpdateView.as_view(), name='product'),
    path('<int:id>/retrieve/', ProductRetrieveView.as_view(), name='product'),
    path('<int:id>/delete/', ProductDeleteView.as_view(), name='product'),
] + product_router.urls
product_image_urlpatterns = [
    path('create/', ProductImageCreateView.as_view(), name='product_image'),
    path('<int:id>/update/', ProductImageUpdateView.as_view(), name='product_image'),
    path('<int:id>/retrieve/', ProductImageRetrieveView.as_view(), name='product_image'),
    path('<int:id>/delete/', ProductImageDeleteView.as_view(), name='product_image'),
] + image_product_router.urls
specification_urlpatterns = [
    path('create/', SpecificationCreateView.as_view(), name='specification'),
    path('<int:id>/update/', SpecificationUpdateView.as_view(), name='specification'),
    path('<int:id>/retrieve/', SpecificationRetrieveView.as_view(), name='specification'),
    path('<int:id>/delete/', SpecificationDeleteView.as_view(), name='specification'),
] + spec_router.urls
