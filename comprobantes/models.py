from django.db import models



IVA = {
    ('Responsable Inscripto','Responsable Inscripto'),
    ('No Inscripto','No Inscripto'),
    ('Exento','Exento'),
    ('No Responsable','No Responsable')
}

class Proveedores(models.Model):
    razon_social = models.CharField(max_length=50)
    domicilio = models.CharField(max_length=100)
    localidad = models.CharField(max_length=50)
    posicion_iva = models.CharField(max_length=50, verbose_name='Posición IVA', choices=IVA)
    cuit = models.CharField(max_length=50)
    estado = models.BooleanField(default=True)

    def __str__(self):
        return self.razon_social


class Factura(models.Model):
    numero = models.CharField(max_length=15)
    fecha = models.DateField()
    razon_social = models.ForeignKey(Proveedores, on_delete=models.CASCADE, verbose_name='Razón Social')
    importe = models.DecimalField(max_digits=10, decimal_places=2)
    iva = models.DecimalField(max_digits=4, decimal_places=2, default=21.0, verbose_name='% IVA')
    estado = models.BooleanField(default=False)
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
    factura_id = models.ForeignKey(Factura,verbose_name='Nº Factura' ,related_name='recibos',           on_delete=models.CASCADE)
    importe_pagado = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    class Meta:
        ordering = ('fecha',)

    @property
    def importe_factura(self):
        return self.factura_id.importe_total
    
    def __str__(self):
        return self.numero


 

