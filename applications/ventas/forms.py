from django import forms


class CotizarServicioForm(forms.Form):

    nombre = forms.CharField(
        max_length=200,
        label = 'Nombre:',
        required = True,
        widget = forms.TextInput(
            attrs={
                'class': 'form-control'
            }
        )
    )
    
    # puesto = forms.CharField(
    #     max_length=400,
    #     label = 'Puesto:',
    #     required = True,
    #     widget = forms.TextInput(
    #         attrs={
    #             'class': 'form-control'
    #         }
    #     )
    # )
