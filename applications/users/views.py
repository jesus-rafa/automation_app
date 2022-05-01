from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import Group
from django.contrib.auth.views import PasswordChangeView
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views.generic import UpdateView, View
from django.views.generic.edit import FormView

from .forms import LoginForm, UserForm
from .models import User


class UpdatePassword(PasswordChangeView):
    form_class = PasswordChangeForm
    success_url = reverse_lazy('users_app:login')
    template_name = 'app/change-password.html'
    template_name = 'users/update.html'


class Perfil(LoginRequiredMixin, UpdateView):
    model = User
    template_name = 'users/perfil.html'
    form_class = UserForm
    success_message = 'Actualizado exitosamente!'

    def get_context_data(self, **kwargs):
        context = super(Perfil, self).get_context_data(**kwargs)

        user = self.request.user.pk

        context['perfil'] = User.objects.get(pk=user)
        #print('yes')

        return context

    def form_valid(self, form):
        #print('yes')

        return super(Perfil, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy('users_app:perfil', kwargs={'pk': self.object.id})


class LoginUser(FormView):
    template_name = 'users/login.html'
    form_class = LoginForm

    def form_valid(self, form):
        user = authenticate(
            email=form.cleaned_data['email'],
            password=form.cleaned_data['password']
        )

        login(self.request, user)

        return super(LoginUser, self).form_valid(form)

    def get_success_url(self):
        user = self.request.user

        obj_groups = Group.objects.filter(user=user.id)

        for group in obj_groups:
            if group.name == 'ADMINISTRADOR':
                return reverse_lazy('home_app:panel-admin')
            else:
                return reverse_lazy('home_app:panel-cliente')


class LogoutView(View):

    def get(self, request, *args, **kwargs):
        logout(request)

        return HttpResponseRedirect(
            reverse(
                'home_app:landing'
            )
        )
