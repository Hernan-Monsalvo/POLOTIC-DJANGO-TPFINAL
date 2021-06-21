from django.db import models
from django.contrib.auth.models import User

# Create your models here.
#cuando creo o modifico un modelo, tengo que migrar para que tome los cambios y agregarlos al archivo admin.py para verlos en panel de djangoadmin
class Producto(models.Model):
    titulo = models.CharField(max_length=64)
    imagen = models.FileField(upload_to='')
    descripcion = models.CharField(max_length=300)
    precio = models.IntegerField()
    categoria = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.titulo} --- ${self.precio}"



class Carrito(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name="carritos")
    productos = models.ManyToManyField(Producto, blank=True, related_name="ventas")
    precioTotal = models.IntegerField()

    def __str__(self):
        return f"{self.id} -- {self.usuario} --- ${self.precioTotal}"


class Categoria(models.Model):
    descripcion = models.CharField(max_length=300)