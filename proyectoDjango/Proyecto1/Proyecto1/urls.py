"""Proyecto1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Proyecto1 import views #importo todo el archivo views
from Proyecto1.views import despedida #importo solo la vista saludo2 del archivo views

urlpatterns = [ #Lista
    path('admin/', admin.site.urls),
    path('saludo/', views.saludo), #primera forma de llamar a una vista del archivo views
    path('despedida/', despedida), #segundo forma de llamar una vista del archivo views
    path('fecha/', views.fecha),
    #path("edades/<int:anio>", views.calcularEdad), #Indico a Django que voy a pasar por la URL un parametro de tipo entero
    path("edades/<int:edad>/<int:anio>", views.calcularEdad), #Ahora con dos parametros
    path("saludoPlantilla/", views.saludoPlantilla),
    path("saludoVariable/<nombre>", views.saludoVariable),
    path("paginaHija/", views.paginaHija),
    path("paginaHija2/", views.paginaHija2),
]
