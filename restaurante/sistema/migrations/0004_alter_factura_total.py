# Generated by Django 5.1.6 on 2025-02-16 22:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sistema', '0003_rename_producto_factura_producto_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='factura',
            name='total',
            field=models.FloatField(editable=False),
        ),
    ]
