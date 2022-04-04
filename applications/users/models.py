from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models

from .managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):

    GENDER_CHOICES = (
        ('M', 'Masculino'),
        ('F', 'Femenino'),
        ('O', 'Otros'),
    )

    email = models.EmailField(unique=True)
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

    USERNAME_FIELD = 'email'

    objects = UserManager()

    def get_full_name(self):
        if self.names and self.last_names:
            return self.names + ' ' + self.last_names
        else:
            return self.email

    def get_initials(self):
        if self.names and self.last_names:
            return self.names[:1].upper() + self.last_names[:1].upper()
        else:
            return ''
