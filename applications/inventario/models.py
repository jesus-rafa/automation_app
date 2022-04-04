from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models


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


class Servicios(models.Model):
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
    contenido = models.TextField(blank=True)
    imagen = models.ImageField(
        'inventario', upload_to="servicios",
        blank=True
    )

    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name = "Servicios"
        verbose_name_plural = "Servicios"
        ordering = ['titulo']


class Producto(models.Model):
    codigo = models.CharField(
        max_length=200,
        blank=True
    )
    nombre = models.CharField(
        max_length=200,
        blank=True
    )
    descripcion = models.CharField(
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
        'contenido',
        blank=True,
        null=True
    )

    def __str__(self):
        return '{}'.format(self.codigo)

    def save(self):
        self.codigo = self.codigo.upper()
        self.nombre = self.nombre.upper()
        self.descripcion = self.descripcion.upper()
        super(Producto, self).save()

    class Meta:
        verbose_name = "Productos"
        verbose_name_plural = "Productos"
        ordering = ['codigo']


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
