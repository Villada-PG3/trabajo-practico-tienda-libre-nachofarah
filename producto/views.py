from django.shortcuts import render
from django.views.generic import TemplateView

class ProductosTemplateView(TemplateView):
    template_name = 'productos.html'

# Create your views here.
def home(request):
    return render(request, "home.html")

def acerca_de_mi(request):
    return render(request, "acerca_de_mi.html")