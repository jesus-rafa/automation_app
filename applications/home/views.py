from applications.inventario.models import (Especificaciones, Producto,
                                            Servicios)
from applications.ventas.forms import CotizarProductoForm, CotizarServicioForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, TemplateView


class Panel_Admin(LoginRequiredMixin, TemplateView):
    """ vista que carga la pagina de inicio """
    template_name = 'home/panel_admin.html'
    login_url = reverse_lazy('users_app:login')


class Panel_Cliente(LoginRequiredMixin, TemplateView):
    """ vista que carga la pagina de inicio """
    template_name = 'home/panel_cliente.html'
    login_url = reverse_lazy('users_app:login')


class Landing(TemplateView):
    """ vista que carga la pagina de inicio """
    template_name = 'landing/inicio.html'

    def get_context_data(self, **kwargs):
        context = super(Landing, self).get_context_data(**kwargs)

        context['servicios'] = Servicios.objects.all()

        context['productos'] = Producto.objects.filter(
            categoria__nombre = 'MUESTRA'
        )
        
        return context


class Ver_Producto(DetailView):
    template_name = 'landing/ver_producto.html'
    model = Producto
    context_object_name = 'producto'

    def get_context_data(self, **kwargs):
        context = super(Ver_Producto, self).get_context_data(**kwargs)
        instancia = self.get_object()

        context['form'] = CotizarProductoForm

        especificaciones = Especificaciones.objects.filter(
            producto = instancia.id
        ).values('agrupador')

        # Tablas de Productos
        agrupador1 = 'Tablero SCI Diesel'
        agrupador2 = 'Tablero SCI Electrica'
        agrupador3 = 'Tablero SCI Jokey'
        agrupador4 = 'Tableros alt-sim para 2 bombas'
        agrupador5 = 'Tableros alt-sim para 3 bombas'
        agrupador6 = 'Tableros vel. var para 2 bombas'
        agrupador7 = 'Tableros vel. var para 3 bombas'

        for row in especificaciones:
            if row['agrupador'] == agrupador1:
                context['agrupador1'] = agrupador1
                context['num_columnas'] = 3
                context['tabla1'] = Especificaciones.objects.filter(
                    producto = instancia.id, 
                    agrupador = agrupador1
                ).values('fases_x_volts', 'baterias', 'modelo')
            
            if row['agrupador'] == agrupador2:
                context['agrupador1'] = agrupador2
                context['num_columnas'] = 3
                context['tabla1'] = Especificaciones.objects.filter(
                    producto = instancia.id,
                    agrupador = agrupador1
                ).values('fases_x_volts', 'baterias', 'modelo')

            if row['agrupador'] == agrupador3:
                context['agrupador1'] = agrupador3
                context['num_columnas'] = 3
                context['tabla1'] = Especificaciones.objects.filter(
                    producto = instancia.id,
                    agrupador = agrupador1
                ).values('fases_x_volts', 'baterias', 'modelo')

            if row['agrupador'] == agrupador4:
                context['agrupador1'] = agrupador4
                context['num_columnas'] = 5
                context['tabla1'] = Especificaciones.objects.filter(
                    producto = instancia.id,
                    agrupador = agrupador4
                ).values('hp','fases_x_volts', 'amp_nom','variador_3', 'variador_1')

            if row['agrupador'] == agrupador5:
                context['agrupador2'] = agrupador5
                context['num_columnas'] = 5
                context['tabla2'] = Especificaciones.objects.filter(
                    producto = instancia.id,
                    agrupador = agrupador5
                ).values('hp','fases_x_volts', 'amp_nom','variador_3', 'variador_1')

            if row['agrupador'] == agrupador6:
                context['agrupador1'] = agrupador6
                context['num_columnas'] = 5
                context['tabla1'] = Especificaciones.objects.filter(
                    producto = instancia.id,
                    agrupador = agrupador6
                ).values('hp','fases_x_volts', 'amp_nom','variador_2', 'variador_1')

            if row['agrupador'] == agrupador7:
                context['agrupador2'] = agrupador7
                context['num_columnas'] = 5
                context['tabla2'] = Especificaciones.objects.filter(
                    producto = instancia.id,
                    agrupador = agrupador7
                ).values('hp','fases_x_volts', 'amp_nom','variador_3', 'variador_1')
        
        return context


class Ver_Servicio(DetailView):
    template_name = 'landing/ver_servicio.html'
    model = Servicios
    context_object_name = 'servicio'

    def get_context_data(self, **kwargs):
        context = super(Ver_Servicio, self).get_context_data(**kwargs)

        context['form'] = CotizarServicioForm
        
        return context
    