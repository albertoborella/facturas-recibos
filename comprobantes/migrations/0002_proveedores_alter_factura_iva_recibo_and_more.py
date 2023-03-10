# Generated by Django 4.1 on 2023-02-04 23:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('comprobantes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Proveedores',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('razon_social', models.CharField(max_length=50)),
                ('domicilio', models.CharField(max_length=100)),
                ('localidad', models.CharField(max_length=50)),
                ('posicion_iva', models.CharField(choices=[('No Inscripto', 'No Inscripto'), ('Responsable Inscripto', 'Responsable Inscripto'), ('No Responsable', 'No Responsable'), ('Exento', 'Exento')], max_length=50, verbose_name='Posición IVA')),
                ('cuit', models.CharField(max_length=50)),
                ('estado', models.BooleanField(default=True)),
            ],
        ),
        migrations.AlterField(
            model_name='factura',
            name='iva',
            field=models.DecimalField(decimal_places=2, default=21.0, max_digits=4, verbose_name='% IVA'),
        ),
        migrations.CreateModel(
            name='Recibo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.CharField(max_length=15)),
                ('fecha', models.DateField()),
                ('importe_pagado', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('factura_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='recibos', to='comprobantes.factura', verbose_name='Nº Factura')),
            ],
            options={
                'ordering': ('fecha',),
            },
        ),
        migrations.AlterField(
            model_name='factura',
            name='razon_social',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='comprobantes.proveedores', verbose_name='Razón Social'),
        ),
    ]
