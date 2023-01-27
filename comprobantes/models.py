from django.db import models

class Factura(models.Model):

    numero = models.CharField(max_length=15)
    fecha = models.DateField()
    razon_social = models.CharField(max_length=50)
    importe = models.DecimalField(max_digits=10, decimal_places=2)
    iva = models.DecimalField(max_digits=4, decimal_places=2, default=21.0)
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

    @property
    def importe_iva(self):
        return self.importe * (self.iva/100)

    @property
    def importe_total(self):
        return self.importe + (self.importe * self.iva/100)

         
    def __str__(self):
        return self.numero


class Recibo(models.Model):
    numero = models.CharField(max_length=15)
    fecha = models.DateField()
    factura_id = models.ForeignKey(Factura,verbose_name='Nº Factura' ,related_name='recibos', on_delete=models.CASCADE)
    importe_pagado = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    @property
    def importe_factura(self):
        return self.factura_id.importe_total

    # @property
    # def saldo_final(self):
    #     return self.saldo_factura - self.importe_pagado
    
    def __str__(self):
        return self.numero
