from django import forms
from django.forms import ModelForm, TextInput
from .models import Factura

class FacturaForm(ModelForm):
    class Meta:
        model = Factura
        fields = ['numero','fecha','razon_social','importe','iva']
        widgets = {
            'numero': TextInput(attrs={'class':'form-control'}),
            'fecha': TextInput(attrs={'class':'form-control'}),
            'razon_social': TextInput(attrs={'class':'form-control'}),
            'importe': TextInput(attrs={'class':'form-control', 'placeholder':'Ingrese el valor sin iva'}),
            'iva': TextInput(attrs={'class':'form-control'}),
        }