
from django.urls import path
from . import views

urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
    path("productos/", views.CatalogoView.as_view(), name="productos"),
    path("producto/<int:pk>/", views.detalle_producto, name="detalle_producto"),
    path("acerca-de-mi/", views.acerca_de_mi, name="acerca_de_mi"),
]
