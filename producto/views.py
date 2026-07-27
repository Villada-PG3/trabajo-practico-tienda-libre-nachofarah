from django.shortcuts import render
from django.views.generic import TemplateView

class ProductosTemplateView(TemplateView):
    template_name = 'productos.html'

# Create your views here.
