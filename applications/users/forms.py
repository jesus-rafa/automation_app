from django import forms
from django.contrib.auth import authenticate

from .models import User


class UserForm(forms.ModelForm):

    names = forms.CharField(
        label='Nombres',
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control'

            }
        )
    )

    last_names = forms.CharField(
        label='Apellidos',
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control'

            }
        )
    )

    telefono = forms.DecimalField(
        label='Telefono:',
        required=False,
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control'
            }
        )
    )

    ext = forms.DecimalField(
        label='Ext:',
        required=False,
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control'
            }
        )
    )

    avatar = forms.FileField(required=False)

    class Meta:
        model = User
        fields = ["names", "last_names", "telefono", "ext", "avatar"]


class LoginForm(forms.Form):
    email = forms.CharField(
        label='Email',
        required=True,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Usuario',
                'class': 'web form-control',
                'placeholder': 'Email',
                'aria-label': 'Email'
            }
        )
    )

    password = forms.CharField(
        label='Contraseña',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Contraseña',
                'class': 'Password form-control',
                'placeholder': 'Contraseña',
                'aria-label': 'Password'
            }
        )
    )

    def clean(self):
        cleaned_data = super(LoginForm, self).clean()
        email = self.cleaned_data['email']
        password = self.cleaned_data['password']

        if not authenticate(email=email, password=password):
            raise forms.ValidationError(
                'Los datos del usuario no son correctos')

        return self.cleaned_data
