from .views import UserViewSet
from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import UserUpdateView

router = DefaultRouter()
router.register('users', UserViewSet, basename='user')

urlpatterns = [
    path('users/<int:id>/', UserUpdateView.as_view(), name='user'),
] + router.urls
