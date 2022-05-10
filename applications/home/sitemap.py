from datetime import datetime, timedelta

#import models
from applications.inventario.models import Producto, Servicios
#
from django.contrib.sitemaps import Sitemap
from django.urls import reverse_lazy


class ProductoSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.8
    protocol = 'https'

    def items(self):
        return Producto.objects.filter(categoria__nombre='MUESTRA')

    def lastmod(self, obj):
        return obj.created


class ServiciosSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.8
    protocol = 'https'

    def items(self):
        return Servicios.objects.all()

    def lastmod(self, obj):
        return obj.created


class Sitemap(Sitemap):
    protocol = 'https'

    def __init__(self, names):
        self.names = names

    def items(self):
        return self.names

    def changefreq(self, obj):
        return 'weekly'

    def lastmod(self, obj):
        return datetime.now()

    def location(self, obj):
        return reverse_lazy(obj)
