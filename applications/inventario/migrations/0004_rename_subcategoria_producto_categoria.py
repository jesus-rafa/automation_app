# Generated by Django 4.0.3 on 2022-03-16 18:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0003_alter_estructura_producto_producto'),
    ]

    operations = [
        migrations.RenameField(
            model_name='producto',
            old_name='subcategoria',
            new_name='categoria',
        ),
    ]
