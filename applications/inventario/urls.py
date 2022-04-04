from django.urls import path

from . import views

app_name = "inventario_app"

urlpatterns = [
    path(
        'productos/',
        views.Productos.as_view(),
        name='productos'
    ),
    path(
        'productos/estructura/',
        views.Estructura.as_view(),
        name='productos-estructura'
    ),
    path(
        'ver-estructura/<int:idProducto>/',
        views.Ver_Estructura.as_view(),
        name='ver-estructura'
    ),
    path(
        'productos/estructura/generar',
        views.Generar_Estructura.as_view(),
        name='generar-estructura'
    ),
    path(
        'batch-productos/',
        views.Batch_Productos.as_view(),
        name='batch-productos'),

    # API INVENTARIO
    path(
        'api/inventario/lista-productos/<str:kword>/',
        views.Lista_Productos.as_view(),
    ),
    path(
        'api/inventario/lista-componentes/<str:kword>/',
        views.Lista_Componentes.as_view(),
    ),

]
