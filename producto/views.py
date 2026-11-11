from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy

from django.shortcuts import render, get_object_or_404, redirect
from datetime import date
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Producto, Categoria
from django.db.models import Q
from .forms import ContactoForm, ProductoForm


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
    paginate_by = 6


def acerca_de_mi(request):
    return render(request, "acerca_de_mi.html")


class DetalleProductoView(DetailView):
    model = Producto
    template_name = "detalle.html"
    context_object_name = "producto"


class CategoriaView(ListView):
    model = Producto
    template_name = "categoria.html"
    context_object_name = "productos"

    def get_queryset(self):
        return Producto.objects.filter(
            categoria__slug=self.kwargs["slug"]
        ).order_by("-fecha_creacion")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categoria"] = get_object_or_404(
            Categoria,
            slug=self.kwargs["slug"]
        )
        return context


def contacto(request):
    """Muestra el formulario (GET) y valida su envío (POST)."""
    enviado = False

    if request.method == "POST":
        form = ContactoForm(request.POST)
        if form.is_valid():
            # Por ahora solo confirmamos los datos válidos; no enviamos emails.
            enviado = True
            form = ContactoForm()
    else:
        form = ContactoForm()

    return render(request, "contacto.html", {"form": form, "enviado": enviado})



def registro(request):
    """Registra al usuario y abre su sesión automáticamente."""
    if request.user.is_authenticated:
        return redirect("catalogo")

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            usuario = form.save()
            login(request, usuario)
            return redirect("catalogo")
    else:
        form = UserCreationForm()

    return render(request, "registration/registro.html", {"form": form})


class ProductoCreateView(LoginRequiredMixin, CreateView):
    model = Producto
    form_class = ProductoForm
    template_name = "producto_form.html"

    def form_valid(self, form):
        form.instance.creado_por = self.request.user
        return super().form_valid(form)


class SoloPropietarioMixin(LoginRequiredMixin, UserPassesTestMixin):
    """Solo el creador del producto o un superusuario puede modificarlo."""

    def test_func(self):
        producto = self.get_object()
        return (self.request.user.is_superuser or
                producto.creado_por_id == self.request.user.pk)


class ProductoUpdateView(SoloPropietarioMixin, UpdateView):
    model = Producto
    form_class = ProductoForm
    template_name = "producto_form.html"


class ProductoDeleteView(SoloPropietarioMixin, DeleteView):
    model = Producto
    template_name = "tiendalibre/producto_confirm_delete.html"
    success_url = reverse_lazy("catalogo")
