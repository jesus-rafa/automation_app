from django.contrib import admin

from .models import Orden_Compra, Orden_Compra_Detalle, Proveedor

admin.site.register(Proveedor)
admin.site.register(Orden_Compra)
admin.site.register(Orden_Compra_Detalle)
