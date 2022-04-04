from django.urls import path

from . import views

app_name = "home_app"

urlpatterns = [
    path('', views.Landing.as_view(), name='landing'),
    path('panel-admin', views.Panel_Admin.as_view(), name='panel-admin'),
    path('panel-cliente', views.Panel_Cliente.as_view(), name='panel-cliente'),

]
