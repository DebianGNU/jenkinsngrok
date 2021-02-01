from django.contrib import admin

from gestionPedidos.models import Clientes, Articulos, Pedidos

# Register your models here.

class ClientesAdmin(admin.ModelAdmin):
    list_display=("nombre", "direccion", "tfno") 
    search_fields=("nombre", "tfno") # creamos el campo de busqueda...

class ArticulosAdmin(admin.ModelAdmin):
    list_filter=("seccion",) # creamos el campo de busqueda de seccion ...

class PedidosAdmin(admin.ModelAdmin):
    list_display=("numero", "fecha")
    list_filter=("fecha",)   # creamos el campo de busqueda por fecha
    date_hierarchy="fecha"  # para busqueda por fecha en la barra ...

admin.site.register(Clientes, ClientesAdmin)
admin.site.register(Articulos, ArticulosAdmin)
admin.site.register(Pedidos, PedidosAdmin)