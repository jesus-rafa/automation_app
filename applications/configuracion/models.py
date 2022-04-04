from django.contrib.auth.models import Group
from django.db import models


class Urls(models.Model):
    url = models.CharField('Url', max_length=100)
    icono = models.CharField('Icono', max_length=100, blank=True, null=True)
    nombre = models.CharField('Nombre', max_length=100, blank=True, null=True)
    padre = models.ForeignKey(
        'self', blank=True, null=True, on_delete=models.CASCADE, related_name="hijos"
    )
    sort = models.IntegerField('Sort', blank=True, null=True)
    nivel = models.IntegerField('Nivel', blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_visible = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Urls'
        verbose_name_plural = 'Urls'
        ordering = ['sort']

    def __str__(self):
        return self.nombre


class Accesos(models.Model):
    perfil = models.ForeignKey(Group, on_delete=models.CASCADE)
    urls = models.ManyToManyField(Urls, blank=True, related_name='get_urls')

    class Meta:
        verbose_name = 'Accesos'
        verbose_name_plural = 'Accesos'
        ordering = ['perfil']

    def __str__(self):
        return str(self.perfil)


class App(models.Model):

    dominio = models.CharField('Dominio', max_length=100, blank=True)
    nombre = models.CharField('Nombre', max_length=200, blank=True)
    logo = models.ImageField(
        'Logo', blank=True, upload_to='configuracion',
    )
    logo_mini = models.ImageField(
        'Logo Mini', blank=True, upload_to='configuracion',
    )
    fondo = models.ImageField(
        'Fondo', blank=True, upload_to='configuracion',
    )

    class Meta:
        verbose_name = 'App'
        verbose_name_plural = 'App'
        ordering = ['dominio']

    def __str__(self):
        return self.dominio
