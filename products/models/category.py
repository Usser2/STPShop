from django.db.models import Model, CharField


class Category(Model):
    name = CharField(verbose_name="категория", unique=True, max_length=100)

    class Meta:
        verbose_name = "категория"
        verbose_name_plural = "категории"

    def __str__(self):
        return self.name
