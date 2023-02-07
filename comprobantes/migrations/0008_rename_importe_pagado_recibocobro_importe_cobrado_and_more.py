# Generated by Django 4.1 on 2023-02-07 20:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('comprobantes', '0007_cliente_alter_facturaventa_unidades_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recibocobro',
            old_name='importe_pagado',
            new_name='importe_cobrado',
        ),
        migrations.AlterField(
            model_name='cliente',
            name='posicion_iva',
            field=models.CharField(choices=[('Responsable Inscripto', 'Responsable Inscripto'), ('No Inscripto', 'No Inscripto'), ('Exento', 'Exento'), ('No Responsable', 'No Responsable')], max_length=50, verbose_name='Posición IVA'),
        ),
        migrations.AlterField(
            model_name='facturaventa',
            name='razon_social',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='comprobantes.cliente', verbose_name='Cliente'),
        ),
        migrations.AlterField(
            model_name='facturaventa',
            name='unidades',
            field=models.CharField(blank=True, choices=[('toneladas', 'toneladas'), ('kilos', 'kilos'), ('litros', 'litros')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='proveedores',
            name='posicion_iva',
            field=models.CharField(choices=[('Responsable Inscripto', 'Responsable Inscripto'), ('No Inscripto', 'No Inscripto'), ('Exento', 'Exento'), ('No Responsable', 'No Responsable')], max_length=50, verbose_name='Posición IVA'),
        ),
    ]