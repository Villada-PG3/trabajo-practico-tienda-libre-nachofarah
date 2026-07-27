from django.contrib import admin
from .models import Producto
from producto.models import categoria

admin.site.register(Producto)
admin.site.register(categoria)

# Register your models here.
