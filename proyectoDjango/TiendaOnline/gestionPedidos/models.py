from django.db import models

# Create your models here.
'''models es un archivo que contiene el modelo de base de datos y las clases aqui creadas 
representan las tablas de la base de datos'''

class Clientes(models.Model):
    #variable nombre de tipo charField -> char
    nombre = models.CharField(max_length=30)
    #verbose_name es el nombre como queremos que aparezca en el Panel de Adminitración
    dirección = models.CharField(max_length=50, verbose_name="La dirección")
    #variable email de tipo email, obligamos a que el cahr contenga @ y un .
    email = models.EmailField(blank=True, null=True)
    telefono = models.CharField(max_length=7)
    
    def __str__(self):
        return self.nombre
    
class Articulos(models.Model):
    nombre = models.CharField(max_length=30)
    seccion = models.CharField(max_length=30)
    precio = models.IntegerField()
    
    #El metodo String me permite dar un formato a como quiero que se vean los datos en el Panel de Adminitración 
    def __str__(self):
        return 'El nombre es %s la sección es: %s y el precio es %s' %(self.nombre,self.seccion,self.precio)
    
class Pedidos(models.Model):
    numero = models.IntegerField()
    fecha = models.DateField()
    entregado = models.BooleanField()    