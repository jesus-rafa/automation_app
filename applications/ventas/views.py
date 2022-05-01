from django.views.generic import TemplateView

from .forms import CotizarServicioForm


class Cotizar_Servicio(TemplateView):
    template_name = 'ventas/cotizar_servicio.html'

    def get_context_data(self, **kwargs):
        context = super(Cotizar_Servicio, self).get_context_data(**kwargs)

        context['form'] = CotizarServicioForm
        
        return context

class Cotizar_Producto(TemplateView):
    template_name = 'ventas/cotizar_producto.html'

    def get_context_data(self, **kwargs):
        context = super(Cotizar_Servicio, self).get_context_data(**kwargs)

        context['form'] = CotizarServicioForm
        
        return context
    