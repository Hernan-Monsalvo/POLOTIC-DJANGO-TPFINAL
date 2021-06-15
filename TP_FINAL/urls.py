from . import views
from django.urls import path

app_name = 'TP_FINAL'

urlpatterns = [
    path('', views.index, name="index"),
    path('login', views.login, name="login"),
    path('registro', views.registro, name="registro"),
    path('producto/<int:id>', views.producto, name="producto"),
    path('nuevoProducto', views.nuevoProducto, name="nuevoProducto"),
    path('editarProducto/<int:id>', views.editarProducto, name="editarProducto"),
    path('eliminarProducto/<int:id>', views.eliminarProducto, name="eliminarProducto"),
    path('carrito', views.carrito, name="carrito"),
    path('busqueda', views.busqueda, name="busqueda"),
    path('acercaDe', views.acercaDe, name="acercaDe"),
    path('media/<str:ruta>', views.media, name="media"),
]
