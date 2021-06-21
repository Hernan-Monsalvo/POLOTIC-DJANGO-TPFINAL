from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from . import models
from django.http import HttpResponse
from .forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.models import Group
from django.db.models import Q


#Rol del usuario
def dameRol(request):
    l = []
    if len(request.user.groups.all()) != 0:
        for g in request.user.groups.all():
            l.append(g.name)
    else:
        return "invitado"
    return l[0]



# Create your views here.
def index(request):
    productos = models.Producto.objects.all()
    primerosTres = productos[len(productos)-3:len(productos)]
    restantes = productos[0:len(productos)-3]
    
    

    return render(request, "tmp/index.html", {
        "primerosTres": primerosTres,
        "restantes": restantes,
        "rol": dameRol(request)
    })

def login(request):
    return HttpResponseRedirect(reverse('login'))

@login_required
def logout(request):
    return HttpResponseRedirect(reverse('logout'))

def registrarse(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            nuevoUsuario = form.save()
            grupoUsuario = Group.objects.get(name='usuario') 
            grupoUsuario.user_set.add(nuevoUsuario)      
            return HttpResponseRedirect(reverse('login'))
    else:
        form = RegistroForm()
    return render(request, 'registration/registro.html', {
        'form': form,
        "rol": dameRol(request)
        })

def producto(request, id):
    producto = models.Producto.objects.get(id=id)

    return render(request, "tmp/producto.html",{
        "producto" : producto,
        "rol": dameRol(request)
    })

@permission_required('TP_FINAL.add_producto')
def nuevoProducto(request):

    if request.method == "POST":
        form = FormAltaProducto(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("TP_FINAL:index"))
        else:
            error = form.errors
            return render(request, "tmp/nuevoProducto.html", {
                "error" : error,
                "rol": dameRol(request)
            })
    else:
        return render(request, "tmp/nuevoProducto.html",{
            "rol": dameRol(request)
        })

@permission_required('TP_FINAL.change_producto')
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
                "error" : error,
                "rol": dameRol(request)
            })
    else:
        return render(request, "tmp/editarProducto.html", {
        "producto":producto,
        "rol": dameRol(request)
        })

@permission_required('TP_FINAL.delete_producto')
def eliminarProducto(request, id):
    producto = models.Producto.objects.get(id=id)
    producto.delete()
    return HttpResponseRedirect(reverse("TP_FINAL:index"))

@login_required
def addCarrito(request, id):
    #producto = models.Producto.objects.get(id=id)

    if "carrito" not in request.session:
        request.session["carrito"] = []

    request.session["carrito"] += [id]

    return HttpResponseRedirect(reverse("TP_FINAL:carrito"))

@login_required
def removeCarrito(request, id):
    #producto = models.Producto.objects.get(id=id)

    lst = request.session["carrito"]
    lst.remove(id)
    request.session["carrito"] = lst

    

    return HttpResponseRedirect(reverse("TP_FINAL:carrito"))

@login_required
def carrito(request):

    if "carrito" not in request.session:
        request.session["carrito"] = []

    carrito = []
    for n in request.session["carrito"]:
        producto = models.Producto.objects.get(id=n)
        carrito.append(producto)

    precioTotal = 0
    for prod in carrito:
        precioTotal += prod.precio

    return render(request, "tmp/carrito.html", {
        "carrito" : carrito,
        "precioTotal": precioTotal,
        "rol": dameRol(request),
        "usuario":request.user.id
    })

@login_required
def realizarCompra(request, id):
    user = User.objects.get(id=id)
    idProductos = request.POST.getlist("productos")
    precioTotal = int(request.POST["precioTotal"])

    carrito = models.Carrito.objects.create(
        usuario=user,
        precioTotal=precioTotal,
    )

    for idP in idProductos:
        carrito.productos.add(models.Producto.objects.get(id=idP))

    carrito.save()

    request.session["carrito"] = []

    return render(request, "tmp/compraExitosa.html", {
            "rol": dameRol(request)
        })

@permission_required('TP_FINAL.view_carrito')
def pedidos(request):

    pedidos = models.Carrito.objects.all()

    return render(request, "tmp/pedidos.html",{
        "rol": dameRol(request),
        "pedidos":pedidos
    })

@permission_required('TP_FINAL.view_carrito')
def detallePedido(request, id):

        pedido = models.Carrito.objects.get(id=id)

        return render(request, "tmp/detallePedido.html",{
        "rol": dameRol(request),
        "pedido":pedido,
    })

def busqueda(request):
    if request.method == "POST":
        busqueda = request.POST["busqueda"]
        resultado =  models.Producto.objects.filter(Q(titulo__contains=busqueda)|Q(categoria__contains=busqueda))

        return render(request, "tmp/busqueda.html", {
            "busqueda" : busqueda,
            "resultado" : resultado,
            "rol": dameRol(request)
        })
    else:
        return render(request, "tmp/busqueda.html",{
            "rol":dameRol(request)
        })


def acercaDe(request):
    return render(request, "tmp/acercaDe.html",{
        "rol": dameRol(request)
    })

def media(request, ruta):
    imagen = open("media/"+ruta, "rb").read()
    return HttpResponse(imagen, content_type="image/png")



