from django.urls import path

from .views import inicio, productos, formProducto, categorias, formCategoria, listarCliente, modificarCategoria, modificarProducto, inicioSesion, registroUsuario



urlpatterns = [

  path('inicio', inicio, name="inicio"),
  path('productos', productos, name="productos"),
  path('formProducto', formProducto, name="formProducto"),
  path('categorias', categorias, name="categorias"),
  path('formCategoria', formCategoria, name="formCategoria"),
  path('listarCliente', listarCliente, name="listarCliente"),
  path('modificarCategoria/<id>', modificarCategoria, name="modificarCategoria"),
  path('modificarProducto/<id>', modificarProducto, name="modificarProducto"),
  path('inicioSesion', inicioSesion, name="inicioSesion"),
  path('registroUsuario', registroUsuario, name="registroUsuario"),



]
# 127.0.0.1:8000
# 127.0.0.1:8000/inicio
# 127.0.0.1:8000/productos
# 127.0.0.1:8000/formProducto
# 127.0.0.1:8000/modificarProducto/100