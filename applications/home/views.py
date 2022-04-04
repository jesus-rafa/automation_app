from applications.inventario.models import Servicios
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
    template_name = 'home/landing.html'

    def get_context_data(self, **kwargs):
        context = super(Landing, self).get_context_data(**kwargs)

        context['servicios'] = Servicios.objects.all()
        
        return context

    