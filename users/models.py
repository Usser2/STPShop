from django.core.validators import RegexValidator
from django.db.models import CharField, EmailField
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth.models import AbstractUser
from django.core.validators import validate_email


class User(AbstractUser):
    username = CharField(verbose_name="логин", max_length=100, unique=True, default="test")
    name = CharField(verbose_name="имя", max_length=100)
    password = CharField(verbose_name="пароль", max_length=100)
    phone_regex = RegexValidator(
        regex=r'^\+\d{1,3}\d{10}$',
        message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."
    )
    phone_number = CharField(
        validators=[phone_regex],
        max_length=17,
        verbose_name="номер телефона",
        unique=True
    )
    email = EmailField(verbose_name="почта", unique=True)

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return f"{self.name} - {self.email}"

    @classmethod
    def create(cls, name, password, phone_number, email):
        if not cls.phone_regex.regex.match(phone_number):
            raise ValueError("Неправильный формат номера телефона")

        if not validate_email(email):
            raise ValueError("Неправильный формат почты")

        hashed_password = make_password(password)

        user = cls(name=name, password=hashed_password, phone_number=phone_number, email=email)
        user.save()

        return user

    @classmethod
    def get_user(cls, email, password):
        if not validate_email(email):
            raise ValueError("Неправильный формат почты")

        user = cls.objects.get(email=email)

        if not check_password(user.password, password):
            raise ValueError("Неправильный пароль")

        return user

    @classmethod
    def delete_user(cls, email, password):
        if not validate_email(email):
            raise ValueError("Неправильный формат почты")

        user = cls.objects.get(email=email)

        if not check_password(user.password, password):
            raise ValueError("Неправильный пароль")

        user.delete()
