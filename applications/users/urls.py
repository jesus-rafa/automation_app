from django.urls import path

from . import views

app_name = "users_app"

urlpatterns = [
    path('login/', views.LoginUser.as_view(), name='login'),
    path('registro/', views.RegistroUser.as_view(), name='registro'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('update/', views.UpdatePassword.as_view(), name='update'),
    path('perfil/<int:pk>/', views.Perfil.as_view(), name='perfil'),
]
