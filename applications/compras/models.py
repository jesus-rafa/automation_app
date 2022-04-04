from applications.inventario.models import Producto
from django.db import models
from django.db.models import Q, Sum
from django.db.models.signals import post_delete, post_save
from model_utils.models import TimeStampedModel


class Proveedor(TimeStampedModel):
    rfc = models.CharField(
        max_length=20,
        unique=True
    )
    nombre = models.CharField(
        max_length=200,
        null=True, blank=True
    )
    apellido = models.CharField(
        max_length=200,
        null=True, blank=True
    )
    direccion = models.CharField(
        max_length=400,
        null=True, blank=True
    )
    telefono = models.CharField(
        max_length=10,
        null=True, blank=True
    )
    telefono2 = models.CharField(
        max_length=10,
        null=True, blank=True
    )
    email = models.CharField(
        max_length=250,
        null=True, blank=True
    )
    email2 = models.CharField(
        max_length=250,
        null=True, blank=True
    )
    is_active = models.BooleanField(default=True)

    def save(self):
        self.rfc = self.rfc.upper()
        super(Proveedor, self).save()

    class Meta:
        verbose_name = 'Provedores'
        verbose_name_plural = 'Provedores'
        ordering = ['rfc']

    def __str__(self):
        return self.rfc

    def get_full_name(self):
        if self.nombre and self.apellido:
            return self.nombre + ' ' + self.apellido
        else:
            return self.nombre


class Orden_Compra(TimeStampedModel):
    fecha_compra = models.DateField(null=True, blank=True)
    comentarios = models.CharField(
        max_length=400,
        null=True, blank=True
    )
    no_factura = models.CharField(max_length=100)
    fecha_factura = models.DateField()
    cantidad = models.PositiveBigIntegerField(default=0)
    subtotal = models.DecimalField(
        'subtotal', decimal_places=2, max_digits=15, blank=True, null=True)
    total = models.DecimalField(
        'total', decimal_places=2, max_digits=15, blank=True, null=True)
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Orden Compra'
        verbose_name_plural = 'Orden Compra'
        ordering = ['no_factura']

    def __str__(self):
        return '{}'.format(self.comentarios)


class Orden_Compra_Detalle(models.Model):
    compra = models.ForeignKey(
        Orden_Compra, related_name='items',
        on_delete=models.CASCADE
    )
    producto = models.ForeignKey(
        Producto,
        on_delete=models.CASCADE
    )
    cantidad = models.PositiveBigIntegerField(
        'cantidad', default=0
    )
    costo = models.DecimalField(
        'costo', decimal_places=2, max_digits=15, blank=True, null=True
    )
    total = models.DecimalField(
        'total', decimal_places=2, max_digits=15, blank=True, null=True
    )

    def __str__(self):
        return '{}'.format(self.compra)

    def save(self, force_insert=False, force_update=False, using=None):
        self.total = float(float(int(self.cantidad)) * float(self.costo))
        super(Orden_Compra_Detalle, self).save()

    class Meta:
        verbose_name = 'Detalle OC'
        verbose_name_plural = 'Detalle OC'
        ordering = ['compra']


def actualizar_compra(sender, instance, **kwargs):
    total = 0
    cantidad = 0

    instancia_compra = Orden_Compra.objects.get(pk=instance.compra.id)

    # obtenemos cantidad y total
    detalle = Orden_Compra_Detalle.objects.filter(
        compra=instance.compra.id
    )

    for item in detalle:
        cantidad = cantidad + item.cantidad
        total = total + item.total

    # actualizamos cantidad y total
    instancia_compra.cantidad = cantidad
    instancia_compra.total = total
    instancia_compra.save()


post_save.connect(actualizar_compra, sender=Orden_Compra_Detalle)
post_delete.connect(actualizar_compra, sender=Orden_Compra_Detalle)
