from django.contrib import admin

from .models import Cliente, Estados, Orden_Venta, Orden_Venta_Detalle

admin.site.register(Cliente)
admin.site.register(Orden_Venta)
admin.site.register(Orden_Venta_Detalle)
admin.site.register(Estados)
