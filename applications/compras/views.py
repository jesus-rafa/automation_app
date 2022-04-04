from applications.inventario.models import Producto
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import (CreateView, DeleteView, ListView,
                                  TemplateView, UpdateView)
from rest_framework.generics import (CreateAPIView, DestroyAPIView,
                                     ListAPIView, UpdateAPIView)
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Orden_Compra, Orden_Compra_Detalle
from .serializers import (CRUDSerializer, DetalleSerializer,
                          OrdenCompraSerializer)


class Ordenes_Compra(LoginRequiredMixin, ListView):
    template_name = 'compras/ordenes_compra.html'
    context_object_name = 'ov'

    def get_queryset(self):

        queryset = Orden_Compra.objects.all().order_by('-fecha_compra')

        return queryset


class Detalle_Orden_Compra(LoginRequiredMixin, TemplateView):
    template_name = 'compras/detalle_ov.html'

    # def get_context_data(self, **kwargs):
    #     context = super(Detalle_Orden_Compra, self).get_context_data(**kwargs)

    #     id = self.kwargs.get('pk')

    #     context['ov'] = Orden_Compra.objects.filter(id=id)

    #     context['detalle'] = Orden_Compra_Detalle.objects.filter(
    #         compra=id
    #     ).order_by('producto')

    #     context['componentes'] = Producto.objects.filter(
    #         categoria__nombre='COMPONENTE'
    #     )

    #     return context


class OV(ListAPIView):
    serializer_class = OrdenCompraSerializer

    def get_queryset(self):
        id_compra = self.kwargs['pk']

        return Orden_Compra.objects.filter(id=id_compra)


class OV_Detalle(ListAPIView):
    serializer_class = DetalleSerializer

    def get_queryset(self):
        id_compra = self.kwargs['id_compra']

        return Orden_Compra_Detalle.objects.filter(compra=id_compra)


class AgregarItem(CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = CRUDSerializer

    def post(self, request, *args, **kwargs):
        serializer = CRUDSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        id_compra = str(serializer.validated_data['compra'])

        instancia_compra = Orden_Compra.objects.get(
            pk=id_compra
        )

        id_producto = str(serializer.validated_data['producto'])

        instancia_producto = Producto.objects.get(
            pk=id_producto
        )

        # agregamos a la compra
        # Orden_Compra_Detalle.objects.create(
        #     compra=instancia_compra,
        #     producto=instancia_producto,
        #     cantidad=serializer.validated_data['cantidad'],
        #     costo=serializer.validated_data['costo']
        # )

        obj, created = Orden_Compra_Detalle.objects.get_or_create(
            compra=instancia_compra,
            producto=instancia_producto,
            defaults={
                'cantidad': serializer.validated_data['cantidad'],
                'costo': serializer.validated_data['costo']
            }
        )

        if obj:
            obj.cantidad = int(obj.cantidad) + \
                int(serializer.validated_data['cantidad'])
            obj.save()

        # update_order(idOrder)

        return Response({'response': 'ok'})


class EditarItem(UpdateAPIView):
    permission_classes = [IsAuthenticated]

    serializer_class = DetalleSerializer
    queryset = Orden_Compra_Detalle.objects.all()

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(
            instance, data=request.data, partial=True
        )
        serializer.is_valid(raise_exception=True)

        serializer.save()

        # update_order(idOrder)
        return Response({'response': 'ok'})


class BorrarItem(DestroyAPIView):
    permission_classes = [IsAuthenticated]

    serializer_class = DetalleSerializer
    queryset = Orden_Compra_Detalle.objects.all()

    def perform_destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
