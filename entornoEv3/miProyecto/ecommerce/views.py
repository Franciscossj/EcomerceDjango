from django.shortcuts import render
from django.shortcuts import redirect
from .models import Producto
from .models import Categoria
from .forms import ProductoForm 
from .forms import CategoriaForm
from .models import Cliente
from .models import Usuario


# Create your views here.
def inicio(request):
    return render(request, 'inicio.html')

def productos(request):
    # buscar orm de django
    listado = Producto.objects.all()
    contexto = {'listado' : listado }
    return render(request, 'productos.html', contexto)

def formProducto(request):
    contexto = { 'form' : ProductoForm }
    if request.method == 'POST':
        producto = ProductoForm(request.POST)
        producto.save() # ... insert


    return render(request, 'formProducto.html', contexto)

def categorias(request):
    # orm de django
    listado = Categoria.objects.all() # select * from Categoria
    contexto = {'listado' : listado, 'usuario' : 'unknow' }
    return render(request, 'categorias.html', contexto)

def formCategoria(request):
    contexto = { 'form' : CategoriaForm }
    if request.method == 'POST':
        categoria = CategoriaForm(request.POST)
        categoria.save()


    return render(request, 'formCategoria.html', contexto)

def listarCliente(request):
    # orm de django
    listado = Cliente.objects.all() # select * from Categoria
    contexto = {'listado' : listado,  }
    return render(request, 'listarCliente.html', contexto)

def modificarCategoria(request, id):
    categoria = Categoria.objects.get(id = id)

    if request.method == 'POST':
        formulario = CategoriaForm(data = request.POST, instance=categoria)
        formulario.save() ## Update

    contexto = { 'form' : CategoriaForm(instance=categoria) }
    return render(request, 'modificarCategoria.html', contexto)

def modificarProducto(request, id):
    producto = Producto.objects.get(id = id)

    if request.method == 'POST':
        formulario = ProductoForm(data = request.POST, instance=producto)
        formulario.save() ## Update

    contexto = { 'form' : ProductoForm(instance=producto) }
    return render(request, 'modificarProducto.html', contexto)

def inicioSesion(request):
    return render(request, 'inicioSesion.html')

def registroUsuario(request):
    # buscar orm de django
    listado = Usuario.objects.all()
    contexto = {'usuario' : 'unknow' }
    return render(request, 'registroUsuario.html', contexto)