from django import forms

# Modelos
from .models import Suscribers, Contact


class SuscribnersForm(forms.ModelForm):

    class Meta:
        model = Suscribers
        fields = ('__all__')
        widgets = {
            'email' : forms.EmailInput(
                attrs={
                    'placeholder' : 'Correo electronico'
                }
            )
        }
        

class ContacForm(forms.ModelForm):

    class Meta:
        model = Contact
        fields = ('__all__')
