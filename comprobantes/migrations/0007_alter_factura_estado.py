# Generated by Django 4.1 on 2023-01-28 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comprobantes', '0006_factura_estado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='factura',
            name='estado',
            field=models.BooleanField(default=True, verbose_name='Saldada'),
        ),
    ]
