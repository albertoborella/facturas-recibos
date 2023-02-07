from django.urls import path
from .views import HomeView, FacturasListView, ReciboView, ReciboCreate, FacturaCreateView,FacturasPagas,FacturasVentaListView,FacturaVentaCreateView,FacturasVentaCobradas,facturasventa_con_saldo,recibos_factura, facturas_con_saldo,cobros_factura


urlpatterns = [
    path('', HomeView.as_view(), name='home'), # Done
    path('facturas/todas/', FacturasListView.as_view(), name='facturas-list'), #Done
    path('facturas-pagas/', FacturasPagas.as_view(), name='facturas-pagas'), #Done
    path('factura/nueva/', FacturaCreateView.as_view(), name='factura-nueva'), #Done
    path('facturas/con_saldo/', facturas_con_saldo, name='facturas-con-saldo'), # Done
    path('recibos-factura/<int:id>', recibos_factura, name='recibos-factura'), # Done
    path('recibos/', ReciboView.as_view(), name='recibos'), # Done
    path('recibo/nuevo/', ReciboCreate.as_view(), name='recibo-crear'),
    path('facturas-venta/todas/', FacturasVentaListView.as_view(), name='facturas-venta-list'),
    path('factura-venta/nueva/', FacturaVentaCreateView.as_view(), name='factura-venta-nueva'),
    path('factura-venta/cobradas/', FacturasVentaCobradas.as_view(), name='factura-venta-cobradas'),
    path('factura-venta/no-cobradas/', facturasventa_con_saldo, name='factura-venta-no-cobradas'),
    path('cobros-factura/<int:id>', cobros_factura, name='cobros-factura'),
]
