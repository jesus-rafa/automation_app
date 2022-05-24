# Generated by Django 3.2.13 on 2022-05-22 04:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='App',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dominio', models.CharField(blank=True, max_length=100, verbose_name='Dominio')),
                ('nombre', models.CharField(blank=True, max_length=200, verbose_name='Nombre')),
                ('logo', models.ImageField(blank=True, upload_to='configuracion', verbose_name='Logo')),
                ('logo_mini', models.ImageField(blank=True, upload_to='configuracion', verbose_name='Logo Mini')),
                ('fondo', models.ImageField(blank=True, upload_to='configuracion', verbose_name='Fondo')),
            ],
            options={
                'verbose_name': 'App',
                'verbose_name_plural': 'App',
                'ordering': ['dominio'],
            },
        ),
        migrations.CreateModel(
            name='Urls',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=100, verbose_name='Url')),
                ('icono', models.CharField(blank=True, max_length=100, null=True, verbose_name='Icono')),
                ('nombre', models.CharField(blank=True, max_length=100, null=True, verbose_name='Nombre')),
                ('sort', models.IntegerField(blank=True, null=True, verbose_name='Sort')),
                ('nivel', models.IntegerField(blank=True, null=True, verbose_name='Nivel')),
                ('is_active', models.BooleanField(default=True)),
                ('is_visible', models.BooleanField(default=True)),
                ('padre', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='hijos', to='configuracion.urls')),
            ],
            options={
                'verbose_name': 'Urls',
                'verbose_name_plural': 'Urls',
                'ordering': ['sort'],
            },
        ),
        migrations.CreateModel(
            name='Accesos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('perfil', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth.group')),
                ('urls', models.ManyToManyField(blank=True, related_name='get_urls', to='configuracion.Urls')),
            ],
            options={
                'verbose_name': 'Accesos',
                'verbose_name_plural': 'Accesos',
                'ordering': ['perfil'],
            },
        ),
    ]
