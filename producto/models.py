from django.db import models
from django.urls import reverse


class Categoria(models.Model):

    nombre = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)

    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"
        ordering = ["nombre"]

    def __str__(self):
        return self.nombre


class Producto(models.Model):

    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.CASCADE,
        related_name="productos",
        null=True,
        blank=True
    )

    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField(default=0)
    marca = models.CharField(max_length=50, default="Marca Desconocida")
    imagen = models.ImageField(upload_to="productos/", null=True, blank=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    activo = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"
        ordering = ["nombre"]

    def __str__(self):
        return f"{self.nombre} - {self.marca} - ${self.precio} - Stock: {self.stock}"

    def get_absolute_url(self):
        """Redirige al detalle del producto después de crearlo o editarlo."""
        return reverse("detalle_producto", kwargs={"pk": self.pk})
