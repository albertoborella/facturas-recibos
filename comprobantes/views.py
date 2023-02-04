from django.shortcuts import render
from django.urls import reverse_lazy
from django.db.models import Sum
from django.views.generic import View,CreateView,ListView
from .models import Recibo, Factura
from .forms import FacturaForm

class HomeView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'comprobantes/base.html')

class FacturasListView(ListView):
    model = Factura


class FacturaCreateView(CreateView):
    model = Factura
    form_class = FacturaForm
    success_url = reverse_lazy('facturas')


class FacturasPagas(ListView):
    model = Factura
    template_name = 'comprobantes/facturas_pagas.html'

    def get_queryset(self):
        return Factura.objects.filter(estado=True)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class ReciboView(View):
    def get(self, request, *args, **kwargs):
        recibos = Recibo.objects.all()
        return render(request, 'comprobantes/recibos.html', { 'recibos':recibos })

def recibos_factura(request, id):
    
    f = Factura.objects.get(id=id)
    recibos = f.recibos.all()
    qs_recibos_pago = Recibo.objects.filter(factura_id=id)
    valor_pagado = 0
    imp_total_factura = f.importe_total
    for p in qs_recibos_pago:
        valor_pagado = valor_pagado + (p.importe_pagado)
    saldo = f.importe_total - valor_pagado
    estado = False
    if saldo == 0.0:
        f.estado = True
        f.save()
    else:
        f.estado = False
        f.save()
    contexto = {'f':f,
                'recibos':recibos,
                'valor_pagado':valor_pagado,
                'saldo':saldo,
                'imp_total_factura':imp_total_factura,
                'estado':estado
                }
    return render(request, 'comprobantes/recibo-factura.html', contexto)


def facturas_con_saldo(request):
    facturas = Factura.objects.filter(estado=False)
    contexto = {
        'facturas':facturas,
    }
    return render(request, 'comprobantes/facturas_con_saldo.html', contexto)




    

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


