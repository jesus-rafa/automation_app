from applications.inventario.models import Producto
from django.db import models
from django.db.models.signals import post_save
from model_utils.models import TimeStampedModel


class Cliente(TimeStampedModel):
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
        super(Cliente, self).save()

    class Meta:
        verbose_name = 'Clientes'
        verbose_name_plural = 'Clientes'
        ordering = ['rfc']

    def __str__(self):
        return self.rfc

    def get_full_name(self):
        if self.nombre and self.apellido:
            return self.nombre + ' ' + self.apellido
        else:
            return self.nombre


class Orden_Venta(TimeStampedModel):
    no_factura = models.CharField(max_length=100)
    fecha_venta = models.DateField(null=True, blank=True)
    comentarios = models.CharField(
        max_length=400,
        null=True, blank=True
    )
    cantidad = models.PositiveBigIntegerField(default=0)
    subtotal = models.DecimalField(
        'subtotal', decimal_places=2, max_digits=15, blank=True, null=True)
    total = models.DecimalField(
        'total', decimal_places=2, max_digits=15, blank=True, null=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Orden Venta'
        verbose_name_plural = 'Orden Venta'
        ordering = ['no_factura']

    def __str__(self):
        return '{}'.format(self.comentarios)


class Orden_Venta_Detalle(models.Model):
    venta = models.ForeignKey(Orden_Venta, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveBigIntegerField(default=0)
    precio = models.DecimalField(
        'precio', decimal_places=2, max_digits=15, blank=True, null=True)
    total = models.DecimalField(
        'total', decimal_places=2, max_digits=15, blank=True, null=True)

    def __str__(self):
        return '{}'.format(self.compra)

    def save(self):
        self.total = float(float(int(self.cantidad)) * float(self.precio))
        super(Orden_Venta_Detalle, self).save()

    class Meta:
        verbose_name = 'Detalle OV'
        verbose_name_plural = 'Detalle OV'
        ordering = ['venta']


# @receiver(post_delete, sender=ComprasDet)
# def detalle_compra_borrar(sender, instance, **kwargs):
#     id_producto = instance.producto.id
#     id_compra = instance.compra.id

#     enc = ComprasEnc.objects.filter(pk=id_compra).first()
#     if enc:
#         sub_total = ComprasDet.objects.filter(
#             compra=id_compra).aggregate(Sum('sub_total'))
#         descuento = ComprasDet.objects.filter(
#             compra=id_compra).aggregate(Sum('descuento'))
#         enc.sub_total = sub_total['sub_total__sum']
#         enc.descuento = descuento['descuento__sum']
#         enc.save()

#     prod = Producto.objects.filter(pk=id_producto).first()
#     if prod:
#         cantidad = int(prod.existencia) - int(instance.cantidad)
#         prod.existencia = cantidad
#         prod.save()


# def update_payments(sender, instance, created, **kwargs):
#     print(" ============= Se actualizo Recaudado =========== ")

#     # if created:
#     pk = str(instance.programa_id)

#     total = Pagos.objects.filter(
#         programa_id=pk,
#         is_active=True
#     ).aggregate(
#         total_recargos=Sum('recargos'),
#         total_accesorios=Sum('accesorios'),
#         total_impuesto=Sum('impuesto')
#     )
#     recaudado = total['total_recargos'] + \
#         total['total_accesorios'] + total['total_impuesto']

#     # print('==============')
#     # print(total)

#     instance = Programa.objects.get(pk=pk)
#     instance.recaudado = recaudado
#     instance.save()

# @receiver(post_save, sender=ComprasDet)
# def detalle_compra_guardar(sender, instance, **kwargs):
#     id_producto = instance.producto.id
#     fecha_compra = instance.compra.fecha_compra

#     prod = Producto.objects.filter(pk=id_producto).first()
#     if prod:
#         cantidad = int(prod.existencia) + int(instance.cantidad)
#         prod.existencia = cantidad
#         prod.ultima_compra = fecha_compra
#         prod.save()


#post_save.connect(update_payments, sender=Pagos)
