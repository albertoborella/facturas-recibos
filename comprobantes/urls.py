from django.urls import path
from .views import HomeView, FacturasListView, ReciboView, FacturaCreateView,FacturasPagas, recibos_factura, facturas_con_saldo


urlpatterns = [
    path('', HomeView.as_view(), name='home'), # Done
    path('facturas/todas/', FacturasListView.as_view(), name='facturas-list'), #Done
    path('facturas-pagas/', FacturasPagas.as_view(), name='facturas-pagas'), #Done
    path('factura/nueva/', FacturaCreateView.as_view(), name='factura-nueva'), #Done
    path('facturas/con_saldo/', facturas_con_saldo, name='facturas-con-saldo'), # Done
    path('recibos-factura/<int:id>', recibos_factura, name='recibos-factura'), # Done
    path('recibos/', ReciboView.as_view(), name='recibos'), # Done
    
]
