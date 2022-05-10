from django.urls import path

from . import views

app_name = "ventas_app"

urlpatterns = [
    path('cotizaciones/', views.Cotizaciones.as_view(), name='cotizaciones'),
    path('cotizar-producto/', views.Cotizar_Producto.as_view(),
         name='cotizar-producto'),
    path('cotizar-servicio/', views.Cotizar_Servicio.as_view(),
         name='cotizar-servicio'),
]
