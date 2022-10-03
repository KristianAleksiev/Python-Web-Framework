from django.urls import path
from django_rest.api.views import ProductsListView, SecondGenericsProductsListView, SingleProductView

urlpatterns = [
      path("products/", ProductsListView.as_view(), name="products list"),
      path("products-generic/", SecondGenericsProductsListView.as_view(), name="products list generic"),
      path("products/<int:pk>/", SingleProductView.as_view(), name="single product"),
]