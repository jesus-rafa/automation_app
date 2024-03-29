# Generated by Django 3.2.13 on 2022-05-22 04:03

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
            name='Orden_Compra',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('fecha_compra', models.DateField(blank=True, null=True)),
                ('comentarios', models.CharField(blank=True, max_length=400, null=True)),
                ('no_factura', models.CharField(max_length=100)),
                ('fecha_factura', models.DateField()),
                ('cantidad', models.PositiveBigIntegerField(default=0)),
                ('subtotal', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True, verbose_name='subtotal')),
                ('total', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True, verbose_name='total')),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Orden Compra',
                'verbose_name_plural': 'Orden Compra',
                'ordering': ['no_factura'],
            },
        ),
        migrations.CreateModel(
            name='Proveedor',
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
                'verbose_name': 'Provedores',
                'verbose_name_plural': 'Provedores',
                'ordering': ['rfc'],
            },
        ),
        migrations.CreateModel(
            name='Orden_Compra_Detalle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.PositiveBigIntegerField(default=0, verbose_name='cantidad')),
                ('costo', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True, verbose_name='costo')),
                ('total', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True, verbose_name='total')),
                ('compra', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='compras.orden_compra')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventario.producto')),
            ],
            options={
                'verbose_name': 'Detalle OC',
                'verbose_name_plural': 'Detalle OC',
                'ordering': ['compra'],
            },
        ),
        migrations.AddField(
            model_name='orden_compra',
            name='proveedor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='compras.proveedor'),
        ),
    ]
