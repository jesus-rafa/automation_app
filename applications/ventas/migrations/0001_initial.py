# Generated by Django 3.2.13 on 2022-05-22 04:07

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('inventario', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('rfc', models.CharField(max_length=20, unique=True)),
                ('nombre', models.CharField(blank=True, max_length=200, null=True)),
                ('apellido', models.CharField(blank=True, max_length=200, null=True)),
                ('direccion', models.CharField(blank=True, max_length=400, null=True)),
                ('telefono', models.CharField(blank=True, max_length=10, null=True)),
                ('telefono2', models.CharField(blank=True, max_length=10, null=True)),
                ('email', models.CharField(blank=True, max_length=250, null=True)),
                ('email2', models.CharField(blank=True, max_length=250, null=True)),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Clientes',
                'verbose_name_plural': 'Clientes',
                'ordering': ['rfc'],
            },
        ),
        migrations.CreateModel(
            name='Estados',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clave', models.CharField(blank=True, max_length=100, verbose_name='Clave')),
                ('nombre', models.CharField(blank=True, max_length=200, verbose_name='Nombre')),
            ],
            options={
                'verbose_name': 'Estados',
                'verbose_name_plural': 'Estados',
                'ordering': ['nombre'],
            },
        ),
        migrations.CreateModel(
            name='Orden_Venta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('no_factura', models.CharField(max_length=100)),
                ('fecha_venta', models.DateField(blank=True, null=True)),
                ('comentarios', models.CharField(blank=True, max_length=400, null=True)),
                ('cantidad', models.PositiveBigIntegerField(default=0)),
                ('subtotal', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True, verbose_name='subtotal')),
                ('total', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True, verbose_name='total')),
                ('is_active', models.BooleanField(default=True)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ventas.cliente')),
            ],
            options={
                'verbose_name': 'Orden Venta',
                'verbose_name_plural': 'Orden Venta',
                'ordering': ['no_factura'],
            },
        ),
        migrations.CreateModel(
            name='Orden_Venta_Detalle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.PositiveBigIntegerField(default=0)),
                ('precio', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True, verbose_name='precio')),
                ('total', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True, verbose_name='total')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventario.producto')),
                ('venta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ventas.orden_venta')),
            ],
            options={
                'verbose_name': 'Detalle OV',
                'verbose_name_plural': 'Detalle OV',
                'ordering': ['venta'],
            },
        ),
    ]