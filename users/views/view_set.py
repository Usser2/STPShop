from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action
from django.contrib.auth.tokens import default_token_generator

from ..models import User


class UserViewSet(ViewSet):
    @action(detail=False, methods=['post'])
    def login(self, request):
        email = request.POST.get("email")
        password = request.POST.get("password")

        if not User.objects.filter(email=email).exists():
            return Response({"message": "User not found"}, status=status.HTTP_401_UNAUTHORIZED)

        try:
            user = User.get_user(email, password)
            response = Response(
                {"message": "Login successful!"},
                status=status.HTTP_202_ACCEPTED
            )
            response.set_cookie("auth_token", default_token_generator.make_token(user))
            return response
        except ValueError:
            return Response({"message": "Invalid email or password!"}, status=status.HTTP_403_FORBIDDEN)

    @action(detail=True, methods=['post'])
    def delete(self, request):
        email = request.get("email")
        password = request.POST.get("password")

        if not User.objects.filter(email=email).exists():
            return Response({"message": "User not found"}, status=status.HTTP_401_UNAUTHORIZED)

        try:
            User.delete_user(email, password)
            return Response(
                {"message": "Deleted successfully."},
                status=status.HTTP_200_OK
            )
        except ValueError:
            return Response({"message": "Invalid email or password!"}, status=status.HTTP_401_UNAUTHORIZED)

    @action(detail=False, methods=['post'])
    def register(self, request):
        username = request.POST.get("username")
        password = request.POST.get("password")
        phone_number = request.POST.get("phone_number")
        email = request.POST.get("email")

        if User.objects.filter(name=username).exists():
            return Response(
                {"message": "User {} already exists!".format(username)},
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            user = User.create(name=username, password=password, phone_number=phone_number, email=email)
            response = Response(
                {"message": "User {} successfully created!".format(username)},
                status=status.HTTP_201_CREATED
            )
            response.set_cookie("auth_token", default_token_generator.make_token(user))
            return response
        except ValueError:
            return Response({"message": "Credentials verification failed!"}, status=status.HTTP_403_FORBIDDEN)
