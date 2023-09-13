from django.db.models import Model, CharField, TextField, IntegerField, DateTimeField


class PromoCode(Model):
    code = CharField(verbose_name="промокод", max_length=100)
    description = TextField(verbose_name="описание", null=True, blank=True)
    percent = IntegerField(verbose_name="скидочный процент")
    expiration_date = DateTimeField(verbose_name="годен до")

    class Meta:
        verbose_name = "промокод"
        verbose_name_plural = "промокоды"

    def __str__(self):
        return f"{self.code} = {self.percent}%"
