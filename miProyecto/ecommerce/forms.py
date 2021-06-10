from django import forms
from django.forms import ModelForm
from .models import Producto
from .models import Categoria
from .models import Cliente


class ProductoForm(ModelForm):

    class Meta:
        model = Producto
        fields = ['id', 'codigoBarra', 'descripcion', 'precioCosto', 'precioVenta', 'stock', 'categoria']

class CategoriaForm(ModelForm):
    
    class Meta:
        model = Categoria
        fields = '__all__' #['codigoBarra','descripcion']

class ClienteForm(ModelForm):
    
    class Meta:
        model = Cliente
        fields = '__all__' #['codigoBarra','descripcion']
    
