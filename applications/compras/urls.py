from django.urls import path

from . import views

app_name = "compras_app"

urlpatterns = [
    path(
        'ordenes-compra/',
        views.Ordenes_Compra.as_view(),
        name='ordenes-compra'
    ),
    path(
        'detalle-ov/<int:pk>/',
        views.Detalle_Orden_Compra.as_view(),
        name='detalle-ov'
    ),
    path(
        'api/compras/ov/<int:pk>/',
        views.OV.as_view(),
    ),
    path(
        'api/compras/agregar-item/',
        views.AgregarItem.as_view(),
    ),
    path(
        'api/compras/editar-item/<int:pk>',
        views.EditarItem.as_view(),
    ),
    path(
        'api/compras/borrar-item/<int:pk>',
        views.BorrarItem.as_view(),
    ),
]
