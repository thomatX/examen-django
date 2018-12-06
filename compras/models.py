from django.db import models

# Create your models here.

class Usuario(models.Model):
    email = models.CharField(max_length = 40, primary_key=True)
    name = models.CharField(max_length = 30)
    age = models.IntegerField()
    password = models.CharField(max_length = 30)

class Lista(models.Model):
    id_pk = models.IntegerField(primary_key=True)
    email = models.CharField(max_length = 40)
    name = models.CharField(max_length = 30)
    total_productos = models.IntegerField()
    total_productos_comprados = models.IntegerField()
    total_presupuestado = models.IntegerField()
    total_real = models.IntegerField()

class Producto(models.Model):
    id_pk = models.IntegerField(primary_key=True)
    name = models.CharField(max_length = 40)
    description = models.CharField(max_length = 400)
    price = models.IntegerField()
    email = models.CharField(max_length = 40)
    image = models.ImageField(upload_to = 'products/', default = 'products/default.png')

class ProductoCliente(models.Model):
    id_producto_cliente = models.IntegerField(primary_key=True)
    id_lista = models.IntegerField()
    id_producto = models.IntegerField()

class Tienda(models.Model):
    id_pk = models.IntegerField(primary_key=True)
    email = models.CharField(max_length = 40)
    name = models.CharField(max_length = 40)
    nombre_sucursal = models.CharField(max_length = 40)
    direccion = models.CharField(max_length = 40)
    ciudad = models.CharField(max_length = 40)
    region = models.CharField(max_length = 40)
