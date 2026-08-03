from django.urls import path
from . import views
from .views import ProductosTemplateView

urlpatterns = [
    path("", views.home, name="home"),
    path("acerca-de-mi/", views.acerca_de_mi, name="acerca_de_mi"),
    path("productos/", ProductosTemplateView.as_view(), name="productos"),
]