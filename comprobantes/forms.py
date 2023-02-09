from django import forms
from django.forms import ModelForm, TextInput, DateInput,Select,DateField
from django.conf import settings
from .models import Factura,Recibo,FacturaVenta,ReciboCobro


class DateInput(forms.DateTimeInput):
    input_type = 'date'


class FacturaForm(ModelForm):
    class Meta:
        model = Factura
        fields = ['numero','fecha','razon_social','importe','iva']
        widgets = {
            'numero': TextInput(attrs={'class':'form-control'}),
            'fecha': DateInput(attrs={'class': 'form-control'}),
            'razon_social': Select(attrs={'class':'form-control'}),
            'importe': TextInput(attrs={'class':'form-control', 'placeholder':'Ingrese el valor sin iva'}),
            'iva': TextInput(attrs={'class':'form-control'}),
        }


class ReciboForm(ModelForm):
    class Meta:
        model = Recibo
        fields = ['numero','factura_id','fecha','importe_pagado']
        widgets = {
            'numero':TextInput(attrs={'class':'form-control'}),
            'factura_id':Select(attrs={'class':'form-control'}),
            'fecha':DateInput(attrs={'class': 'form-control'}),
            'importe_pagado':TextInput(attrs={'class':'form-control'}),
        }

class FacturaVentaForm(ModelForm):
    class Meta:
        model = FacturaVenta
        fields = ['numero','fecha','razon_social','categoria','cantidad','unidades','importe','iva']
        widgets = {
            'numero': TextInput(attrs={'class':'form-control'}),
            'fecha': DateInput(attrs={'class': 'form-control'}),
            'razon_social': Select(attrs={'class':'form-control'}),
            'categoria': Select(attrs={'class':'form-control'}),
            'cantidad': TextInput(attrs={'class':'form-control', 'placeholder':'Ingrese la cantidad'}),
            'unidades': Select(attrs={'class':'form-control'}),
            'importe': TextInput(attrs={'class':'form-control', 'placeholder':'Ingrese el valor sin iva'}),
            'iva': TextInput(attrs={'class':'form-control'}),
        }

class CobroForm(ModelForm):
    class Meta:
        model = ReciboCobro
        fields = ['numero','fecha','factura_id','importe_cobrado']
        widgets = {
            'numero':TextInput(attrs={'class':'form-control'}),
            'fecha':DateInput(attrs={'class': 'form-control'}),
            'factura_id':Select(attrs={'class':'form-control'}),
            'importe_cobrado':TextInput(attrs={'class':'form-control'}),
        }
    