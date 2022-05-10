from applications.inventario.models import Producto, Servicios
from applications.ventas.models import Estados
from django import forms


class CotizarServicioForm(forms.Form):

    nombre = forms.CharField(
        max_length=200,
        label='Nombre*:',
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Nombre...'
            }
        )
    )

    email = forms.CharField(
        max_length=200,
        label='Email*:',
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Email...'
            }
        )
    )

    telefono = forms.CharField(
        max_length=10,
        label='Telefono*:',
        required=True,
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Telefono...'
            }
        )
    )

    nombre_empresa = forms.CharField(
        max_length=200,
        label='Nombre de la Empresa:',
        required=False,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Nombre de la Empresa...'
            }
        )
    )

    giro_empresa = forms.CharField(
        max_length=200,
        label='Giro de la Empresa:',
        required=False,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Giro de la Empresa...'
            }
        )
    )

    servicio = forms.ModelChoiceField(
        queryset=Servicios.objects.all().values_list('titulo', flat=True),
        label='Servicio:',
        initial=0,
        widget=forms.Select(
            attrs={
                'class': 'form-select'
            }
        )
    )

    estado = forms.ModelChoiceField(
        queryset=Estados.objects.all().values_list('nombre', flat=True),
        label='Estado:',
        initial=0,
        widget=forms.Select(
            attrs={
                'class': 'form-select'
            }
        )
    )

    comentarios = forms.CharField(
        max_length=400,
        label='Comentarios:',
        required=False,
        widget=forms.Textarea(
            attrs={
                'class': 'form-control',
                'placeholder': 'Comentarios...',
                'rows': '2'
            }
        )
    )


class CotizarProductoForm(forms.Form):

    nombre = forms.CharField(
        max_length=200,
        label='Nombre*:',
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Nombre...'
            }
        )
    )

    email = forms.CharField(
        max_length=200,
        label='Email*:',
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Email...'
            }
        )
    )

    telefono = forms.CharField(
        max_length=10,
        label='Telefono*:',
        required=True,
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Telefono...'
            }
        )
    )

    nombre_empresa = forms.CharField(
        max_length=200,
        label='Nombre de la Empresa:',
        required=False,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Nombre de la Empresa...'
            }
        )
    )

    giro_empresa = forms.CharField(
        max_length=200,
        label='Giro de la Empresa:',
        required=False,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Giro de la Empresa...'
            }
        )
    )

    producto = forms.ModelChoiceField(
        queryset=Producto.objects.filter(
            categoria__nombre='MUESTRA').values_list('nombre', flat=True),
        label='Producto:',
        initial=0,
        widget=forms.Select(
            attrs={
                'class': 'form-select'
            }
        )
    )

    estado = forms.ModelChoiceField(
        queryset=Estados.objects.all().values_list('nombre', flat=True),
        label='Estado:',
        initial=0,
        widget=forms.Select(
            attrs={
                'class': 'form-select'
            }
        )
    )

    comentarios = forms.CharField(
        max_length=400,
        label='Comentarios:',
        required=False,
        widget=forms.Textarea(
            attrs={
                'class': 'form-control',
                'placeholder': 'Comentarios...',
                'rows': '2'
            }
        )
    )
