from django.core.validators import RegexValidator
from django.db.models import Model, CharField, EmailField


class User(Model):
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
