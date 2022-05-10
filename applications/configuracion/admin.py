from django.contrib import admin

from .models import Accesos, App, Urls

admin.site.register(Accesos)
admin.site.register(Urls)
admin.site.register(App)
