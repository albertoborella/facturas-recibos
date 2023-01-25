from django.urls import path
from .views import HomeView, FacturaView, ReciboView, recibos_factura


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('facturas/', FacturaView.as_view(), name='facturas'),
    path('recibos/', ReciboView.as_view(), name='recibos'),
    path('recibos-factura/<int:id>', recibos_factura, name='recibos-factura'),
]


