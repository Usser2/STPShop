from .category import CategoryCreateView, CategoryUpdateView, CategoryRetrieveView, CategoryDeleteView
from .product import ProductCreateView, ProductUpdateView, ProductRetrieveView, ProductDeleteView
from .product_image import (
    ProductImageCreateView,
    ProductImageUpdateView,
    ProductImageRetrieveView,
    ProductImageDeleteView
)
from .specification import (
    SpecificationCreateView,
    SpecificationUpdateView,
    SpecificationRetrieveView,
    SpecificationDeleteView
)
from .extra_actions import ProductViewSet, ProductImageViewSet, SpecificationViewSet
