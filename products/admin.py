from django.contrib import admin
from .models import Product, Category, Specification


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ["name", "price", "count", "is_for_sale"]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name"]


@admin.register(Specification)
class SpecificationAdmin(admin.ModelAdmin):
    list_display = ["product", "name"]
