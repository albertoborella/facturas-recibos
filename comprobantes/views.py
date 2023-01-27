from django.shortcuts import render
from django.db.models import Sum
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

def recibos_factura(request, id):
    f = Factura.objects.get(id=id)
    recibos = f.recibos.all()
    qs_recibos_pago = Recibo.objects.filter(factura_id=id)
    print(qs_recibos_pago)
    valor_pagado = 0
    for p in qs_recibos_pago:
        valor_pagado = valor_pagado + (p.importe_pagado)
    saldo = f.importe_total - valor_pagado
    imp_total_factura = f.importe_total
    contexto = {'f':f,
                'recibos':recibos,
                'valor_pagado':valor_pagado,
                'saldo':saldo,
                'imp_total_factura':imp_total_factura,}
    return render(request, 'comprobantes/recibo-factura.html', contexto)




    

# def recibos(request, id):
#     f = Factura.objects.get(id=id)
#     recibos = f.recibos.all()
#     pagos = Recibo.objects.aggregate(pagos = Sum('importe_pagado'))
#     imp_total_factura = f.importe_total
    
#     contexto = {
#         'f':f,
#         'recibos':recibos,
#         'pagos':pagos,
#         'imp_total_factura':imp_total_factura,
#     }
    
#     print(pagos)
#     print(imp_total_factura)
    
#     return render(request, 'comprobantes/recibo-factura.html', contexto)

def recibos_factura(request, id):
    f = Factura.objects.get(id=id)
    recibos = f.recibos.all()
    qs_recibos_pago = Recibo.objects.filter(factura_id=id)
    print(qs_recibos_pago)
    valor_pagado = 0
    for p in qs_recibos_pago:
        valor_pagado = valor_pagado + (p.importe_pagado)
    saldo = f.importe_total - valor_pagado
    imp_total_factura = f.importe_total
    contexto = {'f':f,
                'recibos':recibos,
                'valor_pagado':valor_pagado,
                'saldo':saldo,
                'imp_total_factura':imp_total_factura,}
    return render(request, 'comprobantes/recibo-factura.html', contexto)
