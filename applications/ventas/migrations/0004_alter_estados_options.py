# Generated by Django 4.0.3 on 2022-05-04 22:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0003_estados'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='estados',
            options={'ordering': ['nombre'], 'verbose_name': 'Estados', 'verbose_name_plural': 'Estados'},
        ),
    ]
