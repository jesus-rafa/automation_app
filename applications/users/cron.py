from email.mime.image import MIMEImage
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from .models import Enviar_Correos

def generar_correos():
    print('ejecutando cron perro...')

    # Obtener todos los correos que No se han enviado
    obj = Enviar_Correos.objects.filter(is_sent=False)

    # agregar logo en el email
    path = settings.MEDIA_ROOT + '/logo-white.png'
    logo_data = open(path, 'rb')
    logo = MIMEImage(logo_data.read())
    logo_data.close()
    logo.add_header('Content-ID', '<logo>')

    # Enviar correos dependiendo del tipo
    for row in obj:
        if row.tipo == 'GENERAL':

            subject = 'Cotización General: ' + row.nombre
            text_content = ''
            html_content = render_to_string(
                'ventas/email/cotizacion.html',
                {'fecha': row.created, 'contacto': row.nombre,
                    'email': row.correo, 'comentarios': row.comentarios}
            )
            msg = EmailMultiAlternatives(
                subject,
                text_content,
                'ventas@dmingenieria.com.mx',
                [row.correo,'ventas@dmingenieria.com.mx']
            )
            msg.attach_alternative(html_content, "text/html")
            msg.attach(logo)
            msg.send()

        if row.tipo == 'SERVICIO':

            subject = 'Cotización Servicio: ' + row.nombre
            text_content = ''
            html_content = render_to_string(
                'ventas/email/cotizacion_servicio.html',
                {'fecha': row.created, 'contacto': row.nombre, 'email': row.correo, 'comentarios': row.comentarios, 'estado': row.estado,
                 'telefono': row.telefono, 'nombre_empresa': row.nombre_empresa, 'giro_empresa': row.giro_empresa, 'servicio': row.cotizacion}
            )
            msg = EmailMultiAlternatives(
                subject,
                text_content,
                'ventas@dmingenieria.com.mx',
                [row.correo,'ventas@dmingenieria.com.mx']
            )
            msg.attach_alternative(html_content, "text/html")
            msg.attach(logo)
            msg.send()

        if row.tipo == 'PRODUCTO':

            subject = 'Cotización Producto: ' + row.nombre
            text_content = ''
            html_content = render_to_string(
                'ventas/email/cotizacion_producto.html',
                {'fecha': row.created, 'contacto': row.nombre, 'email': row.correo, 'comentarios': row.comentarios, 'estado': row.estado,
                 'telefono': row.telefono, 'nombre_empresa': row.nombre_empresa, 'giro_empresa': row.giro_empresa, 'producto': row.cotizacion}
            )
            msg = EmailMultiAlternatives(
                subject,
                text_content,
                'ventas@dmingenieria.com.mx',
                [row.correo,'ventas@dmingenieria.com.mx']
            )
            msg.attach_alternative(html_content, "text/html")
            msg.attach(logo)
            msg.send()

    # Marcar correos como enviados
    Enviar_Correos.objects.filter(is_sent=False).update(is_sent=True)
