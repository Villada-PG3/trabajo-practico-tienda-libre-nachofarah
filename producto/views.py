from django.shortcuts import render, get_object_or_404

from datetime import date

from django.views.generic import TemplateView

from .models import Producto


class ProductosTemplateView(TemplateView):

    template_name = "catalogo.html"

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)

        context["productos"] = Producto.objects.all().order_by("-fecha_creacion")

        return context


def home(request):

    contexto = {

        "nombre_tienda": "Tienda Libre",

        "mensaje": "Bienvenido a nuestro e-commerce desarrollado con Django.",

        "fecha": date.today(),

        "usuario": "Juan Ignacio Farah",

        # Los 3 productos más recientes cargados desde el admin

        "productos_destacados": Producto.objects.order_by("-fecha_creacion")[:3],

    }

    return render(request, "home.html", contexto)


def acerca_de_mi(request):

    return render(request, "acerca_de_mi.html")


def catalogo(request):

    productos = Producto.objects.all().order_by("-fecha_creacion")

    contexto = {"productos": productos}

    return render(request, "catalogo.html", contexto)


def detalle_producto(request, pk):

    producto = get_object_or_404(Producto, pk=pk)

    contexto = {"producto": producto}

    return render(request, "detalle.html", contexto)