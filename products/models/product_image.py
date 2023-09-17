from django.db.models import Model, ForeignKey, ImageField, IntegerField, CASCADE

from . import Product


class ProductImage(Model):
    product = ForeignKey(verbose_name="товар", to=Product, on_delete=CASCADE)
    image = ImageField(verbose_name="изображение", upload_to="products/images")
    cnt_number = IntegerField(verbose_name="порядковый номер", default=0)

    class Meta:
        verbose_name = "изображение"
        verbose_name_plural = "изображения"

    def __str__(self):
        return self.product
