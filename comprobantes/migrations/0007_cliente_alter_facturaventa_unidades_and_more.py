# Generated by Django 4.1 on 2023-02-06 22:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('comprobantes', '0006_facturaventa_cantidad_facturaventa_unidades_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('razon_social', models.CharField(max_length=50)),
                ('domicilio', models.CharField(max_length=100)),
                ('localidad', models.CharField(max_length=50)),
                ('posicion_iva', models.CharField(choices=[('No Inscripto', 'No Inscripto'), ('Exento', 'Exento'), ('No Responsable', 'No Responsable'), ('Responsable Inscripto', 'Responsable Inscripto')], max_length=50, verbose_name='Posición IVA')),
                ('cuit', models.CharField(max_length=50)),
                ('estado', models.BooleanField(default=True)),
            ],
        ),
        migrations.AlterField(
            model_name='facturaventa',
            name='unidades',
            field=models.CharField(blank=True, choices=[('litros', 'litros'), ('kilos', 'kilos'), ('toneladas', 'toneladas')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='proveedores',
            name='posicion_iva',
            field=models.CharField(choices=[('No Inscripto', 'No Inscripto'), ('Exento', 'Exento'), ('No Responsable', 'No Responsable'), ('Responsable Inscripto', 'Responsable Inscripto')], max_length=50, verbose_name='Posición IVA'),
        ),
        migrations.AlterField(
            model_name='facturaventa',
            name='razon_social',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='comprobantes.cliente', verbose_name='Razón Social'),
        ),
    ]
