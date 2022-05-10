from django import forms


class BatchForm(forms.Form):
    
    archivo = forms.FileField(
        required=True,
        widget=forms.FileInput(
            attrs={
                'class': 'form-control'
            }
        )
    )
