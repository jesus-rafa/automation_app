import datetime
from email.mime.image import MIMEImage

from applications.users.models import Correos, Enviar_Correos
from django.conf import settings
from django.contrib import messages
from django.core.mail import EmailMultiAlternatives
from django.shortcuts import redirect
from django.template.loader import render_to_string
from django.views import View
from django.views.generic import TemplateView


class Cotizaciones(TemplateView):
    template_name = ''

    def post(self, request, *args, **kwargs):

        contacto = request.POST['nombre']
        email = request.POST['email']
        comentarios = request.POST['comentarios']
        fecha = datetime.datetime.today()

        # registrar datos para envio de correos
        Enviar_Correos.objects.create(
            tipo='GENERAL',
            correo=email,
            nombre=contacto,
            comentarios=comentarios
        )

        messages.success(
            self.request, 'Muchas Gracias, Revisaremos tu solicitud y te contactaremos a la brevedad, Excelente día.'
        )

        return redirect(self.request.META['HTTP_REFERER'])


class Cotizar_Servicio(TemplateView):
    template_name = ''

    def post(self, request, *args, **kwargs):

        contacto = request.POST['nombre']
        email = request.POST['email']
        comentarios = request.POST['comentarios']
        fecha = datetime.datetime.today()
        telefono = request.POST['telefono']
        nombre_empresa = request.POST['nombre_empresa']
        giro_empresa = request.POST['giro_empresa']
        servicio = request.POST['servicio']
        estado = request.POST['estado']

        # registrar datos para envio de correos
        Enviar_Correos.objects.create(
            tipo='SERVICIO',
            correo=email,
            nombre=contacto,
            telefono=telefono.replace(' ',''),
            nombre_empresa=nombre_empresa,
            giro_empresa=giro_empresa,
            cotizacion=servicio,
            estado=estado,
            comentarios=comentarios
        )

        messages.success(
            self.request, 'Muchas Gracias, Revisaremos tu solicitud y te contactaremos a la brevedad, Excelente día.'
        )

        return redirect(self.request.META['HTTP_REFERER'])


class Cotizar_Producto(TemplateView):
    template_name = ''

    def post(self, request, *args, **kwargs):

        contacto = request.POST['nombre']
        email = request.POST['email']
        comentarios = request.POST['comentarios']
        fecha = datetime.datetime.today()
        telefono = request.POST['telefono']
        nombre_empresa = request.POST['nombre_empresa']
        giro_empresa = request.POST['giro_empresa']
        producto = request.POST['producto']
        estado = request.POST['estado']

        # registrar datos para envio de correos
        Enviar_Correos.objects.create(
            tipo='PRODUCTO',
            correo=email,
            nombre=contacto,
            telefono=telefono.replace(' ',''),
            nombre_empresa=nombre_empresa,
            giro_empresa=giro_empresa,
            cotizacion=producto,
            estado=estado,
            comentarios=comentarios
        )

        messages.success(
            self.request, 'Muchas Gracias, Revisaremos tu solicitud y te contactaremos a la brevedad, Excelente día.'
        )

        return redirect(self.request.META['HTTP_REFERER'])
