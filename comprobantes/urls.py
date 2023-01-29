from django.urls import path
from .views import HomeView, FacturaView, ReciboView, FacturaCreateView, recibos_factura,   facturas_con_saldo


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('facturas/', FacturaView.as_view(), name='facturas'),
    path('factura/nueva/', FacturaCreateView.as_view(), name='factura-nueva'),
    path('recibos/', ReciboView.as_view(), name='recibos'),
    path('recibos-factura/<int:id>', recibos_factura, name='recibos-factura'),
    path('facturas_con_saldo/', facturas_con_saldo, name='facturas-con-saldo'),

]


