# Generated by Django 4.1 on 2023-01-20 23:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comprobantes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='factura',
            name='iva',
            field=models.DecimalField(decimal_places=2, default=21.0, max_digits=4),
        ),
    ]