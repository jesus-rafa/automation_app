from applications.inventario.models import Producto, Servicios
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import TemplateView


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
    #template_name = 'home/landing.html'

    def get_context_data(self, **kwargs):
        context = super(Landing, self).get_context_data(**kwargs)

        context['servicios'] = Servicios.objects.all()

        context['productos'] = Producto.objects.filter(
            categoria__nombre = 'MUESTRA'
        )
        
        return context


class ProductosView(TemplateView):
    """ vista que carga la pagina de inicio """
    template_name = 'home/productos.html'

    def get_context_data(self, **kwargs):
        context = super(ProductosView, self).get_context_data(**kwargs)

        context['servicios'] = Servicios.objects.all()

        context['productos'] = Producto.objects.all()
        
        return context

class Ver_Producto(TemplateView):
    template_name = 'landing/ver_producto.html'

    def get_context_data(self, **kwargs):
        context = super(Ver_Producto, self).get_context_data(**kwargs)

        pk = self.kwargs.get('pk')
        context['producto'] = Producto.objects.filter(pk = pk)
        
        return context


class Ver_Servicio(TemplateView):
    template_name = 'landing/ver_servicio.html'

    def get_context_data(self, **kwargs):
        context = super(Ver_Servicio, self).get_context_data(**kwargs)

        pk = self.kwargs.get('pk')
        context['servicio'] = Servicios.objects.filter(pk = pk)
        
        return context
    