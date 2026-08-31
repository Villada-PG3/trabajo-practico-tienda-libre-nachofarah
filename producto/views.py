from django.shortcuts import render
from datetime import date
from django.views.generic import TemplateView

class ProductosTemplateView(TemplateView):
    template_name = 'productos.html'


def home(request):

    contexto = {
        "nombre_tienda": "Tienda Libre",
        "mensaje": "Bienvenido a nuestro e-commerce desarrollado con Django.",
        "fecha": date.today(),
        "usuario": "Juan Ignacio Farah",

        "productos_destacados": [
            {
                "nombre": "AirPods Pro",
                "precio": 45000,
                "descripcion": "Auriculares inalámbricos con cancelación de ruido.",
                "disponible": True,
                "imagen": "/MEDIA/productos/airpods.webp"
            },
            {
                "nombre": "Teclado Mecánico",
                "precio": 78000,
                "descripcion": "Switches rojos RGB.",
                "disponible": True,
                "imagen": "/MEDIA/productos/teclado.png"
            },
            {
                "nombre": "Mouse Inalámbrico",
                "precio": None,
                "descripcion": "Diseño ergonómico para oficina.",
                "disponible": False,
                "imagen": "/MEDIA/productos/mousegamer.webp"
            },
            {
                "nombre": "iPhone 17 Pro",
                "precio": 1899000,
                "descripcion": "Pantalla Super Retina XDR, chip A19 Pro y sistema de cámaras profesional.",
                "disponible": True,
                "imagen": "/MEDIA/productos/iphone17pro.webp",
            },
            {
                "nombre": "Samsung Galaxy S25 Ultra",
                "precio": None,
                "descripcion": "Galaxy AI, S Pen integrado y cámara de 200 MP para fotografía de alta calidad.",
                "disponible": False,
                "imagen": "/MEDIA/productos/S25.webp",
            },
            {
                "nombre": "Cable USB-C a Lightning",
                "precio": 24990,
                "descripcion": "Cable compatible con iPhone para carga rápida y transferencia de datos.",
                "disponible": True,
                "imagen": "/MEDIA/productos/cableiphone.webp",
            },
        ]
    }

    return render(request, "home.html", contexto)


def acerca_de_mi(request):
    return render(request, "acerca_de_mi.html")