# Consultas ORM - Clase 5

## 1. Ver todos los productos

```python
Producto.objects.all()
```

## 2. Ver todas las categorías

```python
Categoria.objects.all()
```

## 3. Buscar productos que contengan "iphone"

```python
Producto.objects.filter(nombre__icontains="iphone")
```

## 4. Productos con precio mayor a 100000

```python
Producto.objects.filter(precio__gt=100000)
```

## 5. Productos con precio menor a 50000

```python
Producto.objects.filter(precio__lt=50000)
```

## 6. Excluir productos sin stock

```python
Producto.objects.exclude(stock=0)
```

## 7. Ordenar productos por precio descendente

```python
Producto.objects.order_by("-precio")
```

## 8. Obtener un producto por ID

```python
Producto.objects.get(id=1)
```

## 9. Ver la categoría de un producto

```python
producto = Producto.objects.first()
producto.categoria.nombre
```

## 10. Ver los productos de una categoría

```python
categoria = Categoria.objects.first()
categoria.productos.all()
```