# Generated by Django 4.0.3 on 2022-03-20 01:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0005_alter_producto_options_alter_producto_categoria_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='codigo',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
