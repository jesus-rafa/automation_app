"""
    Automation_app URL Configuration
"""
from applications.home.sitemap import (ProductoSitemap, ServiciosSitemap,
                                       Sitemap)
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
# seo
from django.contrib.sitemaps.views import sitemap
from django.urls import include, path, re_path

urlpatterns_main = [
    path('admin/', admin.site.urls),
    # login google
    path('accounts/', include('allauth.urls')),

    # apps locales
    re_path('', include('applications.users.urls')),
    re_path('', include('applications.home.urls')),
    re_path('', include('applications.ventas.urls')),
    re_path('', include('applications.compras.urls')),
    re_path('', include('applications.inventario.urls')),
    re_path('', include('applications.configuracion.urls')),
    re_path('', include('applications.soporte.urls')),

    # urls para ckeditor
    re_path(r'^ckeditor/', include('ckeditor_uploader.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# objeto site map que genera xml
sitemaps = {
    'site': Sitemap(
        [
            'home_app:index'
        ]
    ),
    'productos': ProductoSitemap,
    'servicios': ServiciosSitemap
}

urlpatterns_sitemap = [
    path(
        'sitemap.xml',
        sitemap,
        {'sitemaps': sitemaps},
        name='django.contrib.sitemaps.views.sitemap'
    )
]

urlpatterns = urlpatterns_main + urlpatterns_sitemap
