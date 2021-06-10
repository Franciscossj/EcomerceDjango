from django.db import models
from django.forms.widgets import PasswordInput

# Create your models here.
class Categoria(models.Model):
    id   = models.IntegerField(primary_key= True)
    nombre = models.CharField(max_length=50)
    activo = models.BooleanField()

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    id          = models.IntegerField(primary_key =True)
    codigoBarra = models.IntegerField()
    descripcion = models.CharField(max_length=50)
    precioCosto = models.IntegerField()
    precioVenta = models.IntegerField()
    stock       = models.IntegerField()
    categoria   = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return self.descripcion

class Cliente(models.Model):
    id          = models.IntegerField(primary_key =True)
    nombre      = models.CharField(max_length=50)
    apellido    = models.CharField(max_length=50)


    def __str__(self):
        return self.nombre + ' ' + self.apellido

class Usuario(models.Model):
    id         = models.IntegerField(primary_key=True)
    rut        = models.CharField(max_length=10)
    nombre     = models.CharField(max_length=50)
    apellido   = models.CharField(max_length=50)
    correo     = models.CharField(max_length=80)
    fechanac   = models.DateField()
    telefono   = models.IntegerField()
    pais       = models.CharField(max_length=20)
    niveleduc  = models.CharField(max_length=20)


    def __str__(self):
        return self.correo

