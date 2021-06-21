from . import views
from django.urls import path

app_name = 'TP_FINAL'

urlpatterns = [
    path('', views.index, name="index"),
    path('login', views.login, name="login"),
    path('logout', views.logout, name="logout"),
    path('registrarse', views.registrarse, name="registrarse"),
    path('producto/<int:id>', views.producto, name="producto"),
    path('nuevoProducto', views.nuevoProducto, name="nuevoProducto"),
    path('editarProducto/<int:id>', views.editarProducto, name="editarProducto"),
    path('eliminarProducto/<int:id>', views.eliminarProducto, name="eliminarProducto"),
    path('carrito', views.carrito, name="carrito"),
    path('addCarrito/<int:id>', views.addCarrito, name="addCarrito"),
    path('removeCarrito/<int:id>', views.removeCarrito, name="removeCarrito"),
    path('realizarCompra/<int:id>', views.realizarCompra, name="realizarCompra"),
    path('pedidos', views.pedidos, name="pedidos"),
    path('detallePedido/<int:id>', views.detallePedido, name="detallePedido"),
    path('busqueda', views.busqueda, name="busqueda"),
    path('acercaDe', views.acercaDe, name="acercaDe"),
    path('media/<str:ruta>', views.media, name="media"),
]
