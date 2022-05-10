import datetime
from email.mime.image import MIMEImage

from applications.users.models import Correos
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

        # registrar correos
        Correos.objects.get_or_create(
            correo=email,
            nombre=contacto,
            is_cotizacion=True
        )

        # agregar logo en el email
        path = settings.MEDIA_ROOT + '/logo-white.png'
        logo_data = open(path, 'rb')
        logo = MIMEImage(logo_data.read())
        logo_data.close()
        logo.add_header('Content-ID', '<logo>')

        # Envio de correo
        subject = 'Cotización: ' + contacto
        text_content = ''
        html_content = render_to_string(
            'ventas/email/cotizacion.html',
            {'fecha': fecha, 'contacto': contacto,
                'email': email, 'comentarios': comentarios}
        )
        msg = EmailMultiAlternatives(
            subject,
            text_content,
            settings.EMAIL_HOST_USER,
            [email]
        )
        msg.attach_alternative(html_content, "text/html")
        msg.attach(logo)
        msg.send()

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

        # registrar correos
        Correos.objects.get_or_create(
            correo=email,
            nombre=contacto,
            is_cotizacion=True
        )

        # agregar logo en el email
        path = settings.MEDIA_ROOT + '/logo-white.png'
        logo_data = open(path, 'rb')
        logo = MIMEImage(logo_data.read())
        logo_data.close()
        logo.add_header('Content-ID', '<logo>')

        # Envio de correo
        subject = 'Cotización Servicio: ' + contacto
        text_content = ''
        html_content = render_to_string(
            'ventas/email/cotizacion_servicio.html',
            {'fecha': fecha, 'contacto': contacto, 'email': email, 'comentarios': comentarios, 'estado': estado,
             'telefono': telefono, 'nombre_empresa': nombre_empresa, 'giro_empresa': giro_empresa, 'servicio': servicio}
        )
        msg = EmailMultiAlternatives(
            subject,
            text_content,
            settings.EMAIL_HOST_USER,
            [email]
        )
        msg.attach_alternative(html_content, "text/html")
        msg.attach(logo)
        msg.send()

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

        # registrar correos
        Correos.objects.get_or_create(
            correo=email,
            nombre=contacto,
            is_cotizacion=True
        )

        # agregar logo en el email
        path = settings.MEDIA_ROOT + '/logo-white.png'
        logo_data = open(path, 'rb')
        logo = MIMEImage(logo_data.read())
        logo_data.close()
        logo.add_header('Content-ID', '<logo>')

        # Envio de correo
        subject = 'Cotización Producto: ' + contacto
        text_content = ''
        html_content = render_to_string(
            'ventas/email/cotizacion_producto.html',
            {'fecha': fecha, 'contacto': contacto, 'email': email, 'comentarios': comentarios, 'estado': estado,
             'telefono': telefono, 'nombre_empresa': nombre_empresa, 'giro_empresa': giro_empresa, 'producto': producto}
        )
        msg = EmailMultiAlternatives(
            subject,
            text_content,
            settings.EMAIL_HOST_USER,
            [email]
        )
        msg.attach_alternative(html_content, "text/html")
        msg.attach(logo)
        msg.send()

        messages.success(
            self.request, 'Muchas Gracias, Revisaremos tu solicitud y te contactaremos a la brevedad, Excelente día.'
        )

        return redirect(self.request.META['HTTP_REFERER'])
