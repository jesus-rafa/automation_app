from datetime import datetime, timedelta

from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse_lazy
from model_utils.models import TimeStampedModel


class Caracteristicas(models.Model):
    """ Model Caracterisicas"""

    caracteristica = models.CharField(
        'Caracteristica',
        unique=True,
        max_length=200,
        blank=True
    )
    descripcion = models.CharField(
        'Descripcion',
        max_length=200,
        blank=True
    )

    class Meta:
        verbose_name = 'Caracteristicas'
        verbose_name_plural = 'Caracteristicas'
        ordering = ['caracteristica']

    def __str__(self):
        return self.caracteristica


class Categoria(models.Model):
    nombre = models.CharField(
        'Categoria',
        max_length=100,
        unique=True
    )
    descripcion = models.CharField(
        max_length=100,
        help_text='Descripción de la Categoría'
    )
    padre = models.ForeignKey(
        'self', blank=True, null=True, on_delete=models.CASCADE, related_name="hijos"
    )

    def __str__(self):
        return self.nombre

    def save(self):
        self.descripcion = self.descripcion.upper()
        super(Categoria, self).save()

    class Meta:
        verbose_name = 'Categorias'
        verbose_name_plural = 'Categorias'
        ordering = ['nombre']


class Marca(models.Model):
    nombre = models.CharField(
        'Marca',
        max_length=100,
        unique=True
    )
    descripcion = models.CharField(
        max_length=100,
        help_text='Descripción de la Marca'
    )

    def __str__(self):
        return self.nombre

    def save(self):
        self.descripcion = self.descripcion.upper()
        super(Marca, self).save()

    class Meta:
        verbose_name = 'Marca'
        verbose_name_plural = 'Marca'
        ordering = ['nombre']


class Unidad_Medida(models.Model):
    unidad = models.CharField(
        'Unidad',
        max_length=100,
        unique=True
    )
    descripcion = models.CharField(
        max_length=100,
        help_text='Descripción de la Unidad Medida'
    )

    def __str__(self):
        return '{}'.format(self.unidad)

    def save(self):
        self.descripcion = self.descripcion.upper()
        super(Unidad_Medida, self).save()

    class Meta:
        verbose_name = 'Unidad Medida'
        verbose_name_plural = 'Unidad Medida'
        ordering = ['unidad']


class Servicios(TimeStampedModel):
    titulo = models.CharField(
        'Título',
        max_length=200,
        unique=True
    )
    subtitulo = models.CharField(
        'Subtítulo',
        max_length=200,
        blank=True
    )
    contenido = models.TextField(
        'Contenido',
        max_length=400,
        blank=True
    )
    estatus = models.CharField(
        'Estatus',
        max_length=100,
        blank=True,
        null=True
    )
    descripcion = models.CharField(
        'Descripcion',
        max_length=200,
        blank=True
    )
    imagen = models.ImageField(
        'imagen', upload_to="servicios",
        blank=True
    )
    slug = models.SlugField(editable=False, max_length=300)
    caracteristicas = models.ManyToManyField(Caracteristicas, blank=True)

    class Meta:
        verbose_name = "Servicios"
        verbose_name_plural = "Servicios"
        ordering = ['titulo']

    def __str__(self):
        return self.titulo

    def get_absolute_url(self):
        return reverse_lazy(
            'home_app:ver-servicio',
            kwargs={
                'slug': self.slug
            }
        )

    def save(self, *args, **kwargs):
        # calculamos el total de segundos de la hora actual
        now = datetime.now()
        total_time = timedelta(
            hours=now.hour,
            minutes=now.minute,
            seconds=now.second
        )
        seconds = int(total_time.total_seconds())
        slug_unique = '%s %s' % (self.titulo, str(seconds))

        self.slug = slugify(slug_unique)

        super(Servicios, self).save(*args, **kwargs)


class Producto(TimeStampedModel):
    codigo = models.CharField(
        'Codigo',
        max_length=200,
        blank=True
    )
    nombre = models.CharField(
        'Nombre',
        max_length=200,
        blank=True
    )
    descripcion = models.CharField(
        'Descripcion',
        max_length=200,
        blank=True
    )
    unidad_medida = models.ForeignKey(
        Unidad_Medida,
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )
    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )
    contenido = RichTextUploadingField(
        'Contenido',
        blank=True,
        null=True
    )
    estatus = models.CharField(
        'Estatus',
        max_length=100,
        blank=True,
        null=True
    )
    imagen = models.ImageField(
        'Imagen', upload_to="productos",
        blank=True
    )
    imagen2 = models.ImageField(
        'Imagen2', upload_to="productos",
        blank=True
    )
    imagen3 = models.ImageField(
        'Imagen3', upload_to="productos",
        blank=True
    )
    slug = models.SlugField(editable=False, max_length=300)
    caracteristicas = models.ManyToManyField(Caracteristicas, blank=True)

    class Meta:
        verbose_name = "Productos"
        verbose_name_plural = "Productos"
        ordering = ['nombre']

    def __str__(self):
        if self.codigo:
            return '{}'.format(self.codigo + '-' + self.nombre)
        if self.nombre:
            return '{}'.format(self.nombre)

    def get_absolute_url(self):
        return reverse_lazy(
            'home_app:ver-producto',
            kwargs={
                'slug': self.slug
            }
        )

    def save(self, *args, **kwargs):
        # calculamos el total de segundos de la hora actual
        now = datetime.now()
        total_time = timedelta(
            hours=now.hour,
            minutes=now.minute,
            seconds=now.second
        )
        seconds = int(total_time.total_seconds())
        slug_unique = '%s %s' % (self.nombre, str(seconds))

        self.slug = slugify(slug_unique)
        self.codigo = self.codigo.upper()

        super(Producto, self).save(*args, **kwargs)


class Estructura_Producto(models.Model):
    producto = models.ForeignKey(
        Producto, on_delete=models.CASCADE, related_name="datos")
    padre = models.ForeignKey(
        'self', blank=True, null=True, on_delete=models.CASCADE, related_name="hijos"
    )
    cantidad = models.PositiveBigIntegerField(default=0)

    def __str__(self):
        return '{}'.format(self.producto)

    class Meta:
        verbose_name = "Estructura Productos"
        verbose_name_plural = "Estructura Productos"
        ordering = ['producto']


class Especificaciones(models.Model):
    producto = models.ForeignKey(
        Producto, on_delete=models.CASCADE, related_name="especificaciones"
    )
    agrupador = models.CharField(
        'Agrupador',
        max_length=100,
        blank=True
    )
    hp = models.IntegerField(default=0)
    fases_x_volts = models.CharField(
        'Fases x Volts',
        max_length=100,
        blank=True
    )
    amp_contactor = models.IntegerField(default=0)
    amp_nom = models.IntegerField(default=0)
    rango_amp_relevador = models.CharField(
        'Rango Amp Relevador',
        max_length=100,
        blank=True
    )
    tension_plena = models.CharField(
        'Tension Plena',
        max_length=100,
        blank=True
    )
    estado_solido = models.CharField(
        'Estado Solido',
        max_length=100,
        blank=True
    )
    baterias = models.IntegerField(default=0)
    hidroneumatico = models.CharField(
        'Hidroneumatico',
        max_length=100,
        blank=True
    )
    carcamo = models.CharField(
        'Carcamo',
        max_length=100,
        blank=True
    )
    modelo = models.CharField(
        'Modelo',
        max_length=100,
        blank=True
    )
    variador_1 = models.CharField(
        'Variador 1',
        max_length=100,
        blank=True
    )
    variador_2 = models.CharField(
        'Variador 2',
        max_length=100,
        blank=True
    )
    variador_3 = models.CharField(
        'Variador 3',
        max_length=100,
        blank=True
    )

    def __str__(self):
        return '{}'.format(self.producto)

    class Meta:
        verbose_name = "Especificaciones"
        verbose_name_plural = "Especificaciones"
        ordering = ['producto']
