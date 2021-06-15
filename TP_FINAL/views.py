from django.forms import fields
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django import forms
from django.urls import reverse
from . import models
from django.http import HttpResponse

#Formularios
class FormAltaProducto(forms.ModelForm):
    
    class Meta:
        model = models.Producto
        fields = ('titulo', 'imagen', 'descripcion', 'precio', 'categoria')

# Create your views here.
def index(request):
    productos = models.Producto.objects.all()
    primerosTres = productos[len(productos)-3:len(productos)]
    restantes = productos[0:len(productos)-3]

    return render(request, "tmp/index.html", {
        "primerosTres": primerosTres,
        "restantes": restantes
    })

def login(request):
    return render(request, "tmp/login.html")

def registro(request):
    return render(request, "tmp/registro.html")

def producto(request, id):
    producto = models.Producto.objects.get(id=id)

    return render(request, "tmp/producto.html",{
        "producto" : producto
    })

def nuevoProducto(request):

    if request.method == "POST":
        form = FormAltaProducto(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("TP_FINAL:index"))
        else:
            error = form.errors
            return render(request, "tmp/nuevoProducto.html", {
                "error" : error
            })
    else:
        return render(request, "tmp/nuevoProducto.html")

    
def editarProducto(request, id):

    producto = models.Producto.objects.get(id=id)


    if request.method == "POST":
        form = FormAltaProducto(request.POST, request.FILES, instance=producto)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("TP_FINAL:index"))
        else:
            error = form.errors
            return render(request, "tmp/editarProducto.html/"+str(id), {
                "error" : error
            })
    else:
        return render(request, "tmp/editarProducto.html", {
        "producto":producto
        })

def eliminarProducto(request, id):
    producto = models.Producto.objects.get(id=id)
    producto.delete()
    return HttpResponseRedirect(reverse("TP_FINAL:index"))

def carrito(request):
    return render(request, "tmp/carrito.html")

def busqueda(request):
    return render(request, "tmp/busqueda.html")

def acercaDe(request):
    return render(request, "tmp/acercaDe.html")

def media(request, ruta):
    imagen = open("media/"+ruta, "rb").read()
    return HttpResponse(imagen, content_type="image/png")



