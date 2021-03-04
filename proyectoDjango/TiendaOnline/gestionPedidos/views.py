from django.shortcuts import render
from django.http import HttpResponse
from gestionPedidos.models import Articulos

# Create your views here.
def buscarProducto(request):
    return render(request,"busqueda_productos.html")

def buscar(request):
    if request.GET['producto']: #Si contiene algo entra
        #mensaje = f"<h1>articulo buscado {request.GET['producto']}</h1>"
        producto = request.GET['producto']
        
        if len(producto)<20:    
            #La Función __icontains permite hacer una busqueda like en la base de datos
            articulos = Articulos.objects.filter(nombre__icontains=producto)
            
            contexto = {"articulos":articulos, "query":producto}
            
            return render(request, "resultados_busqueda.html",contexto)
        else:
            mensaje = "Ha superado la cantidad de caracteres permitidos para la busqueda"
    else:
        mensaje = "No han introducido ningun texto"
    return HttpResponse(mensaje)

def contacto(request):
    
    '''La primera vez que ingresa es por medio de url y no entra al if por que no se envio ningun methodo POST
    pero cuando el usuario presiona en el boton edl formulario ahi redirecciona a la misma view contacto pero con
    un methodo POST por lo que si entrara al if y redireccionara al html gracias.html'''
    if request.method=="POST":
        return render(request,"gracias.html")
    return render(request,"contacto.html")