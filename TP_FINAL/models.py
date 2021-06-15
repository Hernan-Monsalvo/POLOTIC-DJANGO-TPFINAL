from django.db import models

# Create your models here.
#cuando creo un modelo, tengo que migrar para que tome los cambios
class Producto(models.Model):
    titulo = models.CharField(max_length=64)
    imagen = models.FileField(upload_to='')
    descripcion = models.CharField(max_length=300)
    precio = models.IntegerField()
    categoria = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.id} -- {self.titulo} --- ${self.precio}"


# class categoria(models.Model):
#     titulo = models.CharField(max_length=64)
#     descripcion = models.CharField(max_length=124)

# class categoria(models.Model):
#     usuario = models.CharField(max_length=64)
#     productos = models.CharField(max_length=124)
#     precio = models.IntegerField()