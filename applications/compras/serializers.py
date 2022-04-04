from applications.inventario.serializers import ProductoSerializer
from rest_framework import serializers

from .models import Orden_Compra, Orden_Compra_Detalle


class CRUDSerializer(serializers.Serializer):

    compra = serializers.IntegerField()
    producto = serializers.IntegerField()
    cantidad = serializers.IntegerField()
    costo = serializers.DecimalField(max_digits=8, decimal_places=2)


class DetalleSerializer(serializers.ModelSerializer):
    producto = ProductoSerializer()

    class Meta:
        model = Orden_Compra_Detalle
        fields = (
            'id',
            'producto',
            'cantidad',
            'costo',
            'total'
        )


class OrdenCompraSerializer(serializers.ModelSerializer):
    items = DetalleSerializer(many=True)

    class Meta:
        model = Orden_Compra
        fields = (
            'id',
            'fecha_factura',
            'cantidad',
            'subtotal',
            'total',
            'proveedor',
            'items'
        )
