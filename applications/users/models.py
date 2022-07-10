from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from model_utils.models import TimeStampedModel

from .managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):

    GENDER_CHOICES = (
        ('M', 'Masculino'),
        ('F', 'Femenino'),
        ('O', 'Otros'),
    )

    username = models.EmailField(unique=True)
    names = models.CharField('Nombres', max_length=100, blank=True, null=True)
    last_names = models.CharField(
        'Apellidos', max_length=200, blank=True, null=True)
    gender = models.CharField(
        max_length=1,
        choices=GENDER_CHOICES,
        blank=True,
        null=True
    )
    date_birth = models.DateField(
        'Fecha de nacimiento',
        blank=True,
        null=True
    )
    avatar = models.ImageField(
        'Avatar', blank=True, null=True, upload_to='users',
    )
    telefono = models.CharField(
        'Telefono', max_length=10, blank=True, null=True)
    ext = models.CharField('Ext', max_length=5, blank=True, null=True)
    is_staff = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = 'username'

    objects = UserManager()

    def get_full_name(self):
        if self.names and self.last_names:
            return self.names + ' ' + self.last_names
        else:
            return self.username

    def get_initials(self):
        if self.names and self.last_names:
            return self.names[:1].upper() + self.last_names[:1].upper()
        else:
            return ''


class Correos(models.Model):
    correo = models.EmailField('Correo', unique=True)
    nombre = models.CharField('Nombre', max_length=200, blank=True)
    is_cotizacion = models.BooleanField(default=False)
    is_venta = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Correos'
        verbose_name_plural = 'Correos'
        ordering = ['correo']

    def __str__(self):
        return self.correo


class Enviar_Correos(TimeStampedModel):
    correo = models.EmailField('Correo', max_length=200, blank=True)
    nombre = models.CharField('Nombre', max_length=200, blank=True)
    telefono = models.CharField('Telefono', max_length=10, blank=True, null=True)
    nombre_empresa = models.CharField('Nombre Empresa', max_length=200, blank=True)
    giro_empresa = models.CharField('Giro Empresa', max_length=400, blank=True)
    estado = models.CharField('Estado', max_length=200, blank=True)
    tipo = models.CharField('Tipo', max_length=200, blank=True)
    cotizacion = models.CharField('Cotizacion', max_length=600, blank=True)
    is_sent = models.BooleanField(default=False)
    comentarios = models.CharField(
        'Comentarios',
        max_length=800,
        null=True,
        blank=True
    )

    class Meta:
        verbose_name = 'Enviar_Correos'
        verbose_name_plural = 'Enviar_Correos'
        ordering = ['correo']

    def __str__(self):
        return self.correo

