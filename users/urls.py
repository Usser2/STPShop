from .views import UserViewSet
from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import UserUpdateView, UserDeleteView

user_router = DefaultRouter()
user_router.register('', UserViewSet, basename='user-view-set')

urlpatterns = [
    path('<int:id>/', UserUpdateView.as_view(), name='user'),
    path('<int:id>/delete/', UserDeleteView.as_view(), name='user'),
] + user_router.urls
