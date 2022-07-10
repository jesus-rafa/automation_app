from distutils import core

from django.contrib import admin

from .models import Correos, User, Enviar_Correos

admin.site.register(User)
admin.site.register(Correos)
admin.site.register(Enviar_Correos)
