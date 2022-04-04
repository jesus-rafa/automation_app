from django.contrib import admin

from .models import (Categoria, Estructura_Producto, Marca, Producto,
                     Servicios, Unidad_Medida)

admin.site.register(Servicios)
admin.site.register(Producto)
admin.site.register(Estructura_Producto)
admin.site.register(Marca)
admin.site.register(Unidad_Medida)
admin.site.register(Categoria)
