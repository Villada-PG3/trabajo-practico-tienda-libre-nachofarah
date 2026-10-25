
from django.urls import path
from . import views

urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
    path("catalogo/", views.CatalogoView.as_view(), name="catalogo"),
    path(
        "producto/<int:pk>/",
        views.DetalleProductoView.as_view(),
        name="detalle_producto"
    ),
    path("acerca-de-mi/", views.acerca_de_mi, name="acerca_de_mi"),
    path(
    "categoria/<slug:slug>/",
    views.CategoriaView.as_view(),
    name="categoria"
),
]