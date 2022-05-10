from distutils import core

from django.contrib import admin

from .models import Correos, User

admin.site.register(User)
admin.site.register(Correos)
