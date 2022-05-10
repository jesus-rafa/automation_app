from django.urls import path

from . import views

app_name = "home_app"

urlpatterns = [
    path(
        '',
        views.Landing.as_view(), name='index'
    ),
    path(
        'ver-producto/<slug>/',
        views.Ver_Producto.as_view(), name='ver-producto'
    ),
    path(
        'ver-servicio/<slug>/',
        views.Ver_Servicio.as_view(), name='ver-servicio'
    ),
    path(
        'panel-admin/',
        views.Panel_Admin.as_view(), name='panel-admin'
    ),
    path(
        'panel-cliente/',
        views.Panel_Cliente.as_view(), name='panel-cliente'
    ),

]
