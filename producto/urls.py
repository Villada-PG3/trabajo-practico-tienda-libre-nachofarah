
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
    path("contacto/", views.contacto, name="contacto"),
    path("accounts/registro/", views.registro, name="registro"),
    path("producto/nuevo/", views.ProductoCreateView.as_view(), name="producto_nuevo"),
    path("producto/<int:pk>/editar/", views.ProductoUpdateView.as_view(), name="producto_editar"),
    path("producto/<int:pk>/eliminar/", views.ProductoDeleteView.as_view(), name="producto_eliminar"),
    path(
    "categoria/<slug:slug>/",
    views.CategoriaView.as_view(),
    name="categoria"
),
]
