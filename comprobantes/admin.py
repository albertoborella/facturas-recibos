from django.contrib import admin
from .models import Factura,Recibo,Proveedores


class ProveedoresAdmin(admin.ModelAdmin):
    list_display = ('razon_social','domicilio','localidad','posicion_iva','cuit','estado')
    ordering = ('razon_social',)

class FacturaAdmin(admin.ModelAdmin):
    list_display = ('numero','fecha','razon_social','importe','iva','importe_total')
    readonly_fields = ('created','updated')
    ordering = ('-fecha',)

class ReciboAdmin(admin.ModelAdmin):
    list_display = ('numero','fecha','factura_id','importe_factura','importe_pagado')
    ordering = ('fecha',)

admin.site.register(Proveedores,ProveedoresAdmin)
admin.site.register(Factura,FacturaAdmin)
admin.site.register(Recibo,ReciboAdmin)

