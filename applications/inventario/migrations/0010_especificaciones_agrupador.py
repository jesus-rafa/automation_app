# Generated by Django 4.0.3 on 2022-05-01 20:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0009_especificaciones'),
    ]

    operations = [
        migrations.AddField(
            model_name='especificaciones',
            name='agrupador',
            field=models.CharField(blank=True, max_length=100, verbose_name='Agrupador'),
        ),
    ]