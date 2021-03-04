from django.contrib import admin

# Register your models here.
from gestionPedidos.models import Clientes
from gestionPedidos.models import Articulos
from gestionPedidos.models import Pedidos

#Clase que hereda de ModelAdmin, la cual permite hacer modificaiones en los modelos que se trabajan en el Panel de Adm
class ClientesAdmin(admin.ModelAdmin):
    list_display=("nombre","dirección","telefono")
    search_fields=("nombre","telefono")
    
class ArticulosAdministrador(admin.ModelAdmin):
    list_filter=("seccion",)
    
class PedidosAdministrador(admin.ModelAdmin):
    list_display=("numero","fecha","entregado")
    search_fields=("numero","fecha")
    list_filter=("fecha",)
    date_hierarchy=("fecha")
    
#Agregamos modelos en el panel de adminitración
admin.site.register(Clientes, ClientesAdmin)
admin.site.register(Articulos, ArticulosAdministrador)
admin.site.register(Pedidos, PedidosAdministrador)

