from django.shortcuts import render
from django.views.generic import View
from .models import Recibo, Factura


class HomeView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'comprobantes/base.html')

class FacturaView(View):
    def get(self, request, *args, **kwargs):
        facturas = Factura.objects.all()
        return render(request, 'comprobantes/facturas.html', {'facturas':facturas })

class ReciboView(View):
    def get(self, request, *args, **kwargs):
        recibos = Recibo.objects.all()
        return render(request, 'comprobantes/recibos.html', { 'recibos':recibos })

# class RecibosListView(View):
#     def get(self, request, id, *args, **kwargs):
#         fact = Factura.objects.filter(id=id)
#         recibos = fact.recibos.all()
#         return render(request, 'comprobantes/recibos-factura.html', {'recibos':recibos, 'fact':fact})

def recibos_factura(request, id):
    f = Factura.objects.get(id=id)
    recibos = f.recibos.all()
    
    return render(request, 'comprobantes/recibo-factura.html', {'f':f, 'recibos':recibos})
