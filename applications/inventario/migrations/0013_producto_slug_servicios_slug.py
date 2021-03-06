# Generated by Django 4.0.3 on 2022-05-05 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0012_alter_producto_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='slug',
            field=models.SlugField(default='test', editable=False, max_length=300),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='servicios',
            name='slug',
            field=models.SlugField(default='servicios', editable=False, max_length=300),
            preserve_default=False,
        ),
    ]
