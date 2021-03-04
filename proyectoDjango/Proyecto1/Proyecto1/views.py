from django.http import HttpResponse
import datetime
from django.template import Template, Context
from django.template import loader #cargador de plantillas
from django.shortcuts import render #permite simplificar mas el codigo a la hora de renerizar 

#A cada función que se encuentre dentro del archivo views se le donomina vista.
#Las siguientes vistas son a modo de ejemplo ya que el codigo de diseño y el codigo logico siempre deben estar aparte
def saludo(request): 
    
    documento = """
    <html>
        <body>
            <h1>Bienvenido</h1>
        </body>
    </html>"""
    
    return HttpResponse(documento)

def despedida(request): 
    return HttpResponse("Hasta luego")

def fecha(request):
    fecha_actual = datetime.datetime.now()
    
    #Primera forma de agregra una variable a un string
    documento = f"""
    <html>
        <body>
            <h1>Fecha y hora actual{fecha_actual}</h1>
        </body>
    </html>"""
    
    #Segunda forma de agregar una variable a un string 
    documento = """
    <html>
        <body>
            <h2>Fecha y hora actual %s</h2>
        </body>
    </html>""" % fecha_actual
    
    return HttpResponse(documento)

def calcularEdad(request, edad, anio):
    
    periodo = anio-2021
    edadFutura = edad+periodo
    
    #Primera forma de añadir variables a Strings
    documento = f"""
    <html>
        <body>
            <h3>En el año {anio} tendra {edadFutura} años</h3>
        </body>
    </html>"""
    
    #Segunda forma de añadir variables a Stings
    documento = """
    <html>
        <body>
            <h3>En el año %s tendra %s años</h3>
        </body>
    </html>""" %(anio, edadFutura)
    
    return HttpResponse(documento)
    
#FORMA CORRECTA DE CREAR UNA VISTA CON LA LOGICA Y LO VISUAL APARTE
#cargamos la plantilla de manera manual
def saludoPlantilla(request):
    
    #abrimos el archivo
    doc_externo = open("C:/Users/Usuario/Desktop/Curso Django/proyectoDjango/Proyecto1/Proyecto1/Templates/plantillaSaludo.html")
    
    plt = Template(doc_externo.read()) #almacenamos el archivo HTML
    
    doc_externo.close() #cerramos la comunicación, para no consumir recursos
    
    #variable contexto que contiene variables y funciones que se insertan en el template, en este caso no hay ninguna variable
    contexto = Context()
    
    #renderizamos 
    documento = plt.render(contexto)  
    
    return HttpResponse(documento)

#Utilizando cargadores de plantilla
def saludoVariable(request, nombre):
    
     apellido = "Gonzalez"
     
     persona = Persona(nombre,apellido)
     fecha = datetime.datetime.now()
     
     lista_datos = ["Santiago","Alejandro","Gonzalez",22,"o+"]
     lista_datos2 = []
     
     '''CARGADOR DE PLANTILLAS MANUAL
     doc_externo = open("C:/Users/Usuario/Desktop/Curso Django/proyectoDjango/Proyecto1/Proyecto1/Plantillas/plantillaSaludo.html")
     plt = Template(doc_externo.read())
     doc_externo.close()'''
     
     '''CARGADOR DE PLANTILLS 1
     necesita configurar archivo settings.py para asignar la carpeta de nuestras plantillas o templates
     esto lo hacemos en la lista TEMPLATES dentro del camp DIRS['Direccion de la carpeta de templates']
     
     doc_externo = loader.get_template('plantillaSaludo.html')
     contexto = {
         "nombre_persona":nombre,
         "apellido_persona":apellido,
         "fecha":fecha,
         "persona":persona,
         "datos_persona":lista_datos,
         "datos_persona2": lista_datos2,}
     
     documento = doc_externo.render(contexto)'''
     
     contexto = {
         "nombre_persona":nombre,
         "apellido_persona":apellido,
         "fecha":fecha,
         "persona":persona,
         "datos_persona":lista_datos,
         "datos_persona2": lista_datos2,}
     
     #Cargador de plantillas simplicado
     '''Gracias al metodo render de la libreria shortcuts podemos renderizar un template y enviarle el contexto
     de la siguiente manera, haciendo en el return render(request, "nombre de plantilla", contexto si tiene)'''
     return render(request, "plantillaSaludo.html", contexto)
 
def paginaHija(request):
    fecha = datetime.datetime.now()
    return render(request, "paginaHija.html", {"fecha":fecha})

def paginaHija2(request):
    return render(request, "paginaHija2.html")
    

class Persona(object):
    
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido
        