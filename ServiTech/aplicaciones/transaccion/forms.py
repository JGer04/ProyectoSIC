from django import forms
from .models import *
from aplicaciones.cuenta.models import cuenta

class TransaccionForm(forms.ModelForm):
    calcular_iva = forms.BooleanField(label='iva', required=False)
    class Meta:
        model = transaccion
        fields = ['tipo','codigo','fecha','descripcion','cuenta_Debe','cuenta_Haber','monto']

    tipo = forms.ChoiceField(
        widget=forms.RadioSelect, choices= transaccion.CLASIFICACIONES,
        label = 'Tipo de Transacción'
    )

    cuenta_Debe = forms.ModelChoiceField(
        queryset=cuenta.objects.all(),
        label='Cuenta 1'  # Etiqueta personalizada para el campo 'cuenta_Debe'
    )
    
    cuenta_Haber = forms.ModelChoiceField(
        queryset=cuenta.objects.all(),
        label='Cuenta 2'  # Etiqueta personalizada para el campo 'cuenta_Haber'
    )

    def __init__(self, *args, **kwargs):
        super(TransaccionForm, self).__init__(*args, **kwargs)
        self.fields['cuenta_Debe'].queryset = cuenta.objects.all()
        self.fields['cuenta_Haber'].queryset = cuenta.objects.all()