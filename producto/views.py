
from django.shortcuts import render, get_object_or_404
from datetime import date
from django.views.generic import TemplateView, ListView
from .models import Producto


class HomeView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["nombre_tienda"] = "Tienda Libre"
        context["mensaje"] = "Bienvenido a nuestro e-commerce desarrollado con Django."
        context["fecha"] = date.today()
        context["usuario"] = "Juan Ignacio Farah"
        context["productos_destacados"] = Producto.objects.order_by("-fecha_creacion")[:3]
        return context


class CatalogoView(ListView):
    model = Producto
    template_name = "catalogo.html"
    context_object_name = "productos"
    queryset = Producto.objects.all().order_by("-fecha_creacion")


def acerca_de_mi(request):
    return render(request, "acerca_de_mi.html")


def detalle_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    return render(request, "detalle.html", {"producto": producto})
