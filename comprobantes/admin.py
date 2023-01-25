from django.contrib import admin
from .models import Factura,Recibo

class FacturaAdmin(admin.ModelAdmin):
    list_display = ('numero','fecha','razon_social','importe','iva','importe_total')
    readonly_fields = ('created','updated')
    ordering = ('-fecha',)

class ReciboAdmin(admin.ModelAdmin):
    list_display = ('numero','fecha','factura_id','importe_factura','importe_pagado','saldo_factura','saldo_final')
    #readonly_fields = ('created','updated')
    ordering = ('fecha',)

admin.site.register(Factura,FacturaAdmin)
admin.site.register(Recibo,ReciboAdmin)

