from django.db import models

class categoria(models.Model):
    nombre = models.CharField(max_length=100, unique=True) 
    slug = models.SlugField (unique=True)

    class Meta:
        verbose_name = 'categoria'
        verbose_name_plural = 'categorias'
        ordering = ['nombre']

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    categoria = models.ForeignKey(
        categoria,
        on_delete=models.CASCADE,
        related_name='productos',
        null=True,
        blank=True
    )
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)
    imagen = models.ImageField(upload_to='productos/', null=True, blank=True)
    activo = models.BooleanField(default=True)


    def __str__(self):
        return self.nombre

# Create your models here.
