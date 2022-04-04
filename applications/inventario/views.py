import csv
import os

from django.conf import settings
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Case, Count, Sum, When
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.views.generic import (CreateView, DeleteView, ListView,
                                  TemplateView, UpdateView)
from rest_framework.generics import CreateAPIView, ListAPIView, UpdateAPIView

from .forms import BatchForm
from .models import Categoria, Estructura_Producto, Producto
from .serializers import ProductoSerializer


class Productos(LoginRequiredMixin, ListView):
    template_name = 'inventario/productos.html'
    context_object_name = 'productos'

    def get_queryset(self):

        queryset = Producto.objects.all().order_by('codigo')

        return queryset


class Estructura(LoginRequiredMixin, ListView):
    template_name = 'inventario/producto_estructura.html'
    context_object_name = 'productos'

    def get_queryset(self):

        queryset = Estructura_Producto.objects.filter(
            producto__categoria__nombre='PRODUCTO TERMINADO'
        ).annotate(
            sum_componentes=Count('hijos')
        ).order_by('id')

        return queryset


class Ver_Estructura(LoginRequiredMixin, TemplateView):
    template_name = 'inventario/consulta/ver_estructura.html'

    def get_context_data(self, **kwargs):
        context = super(Ver_Estructura, self).get_context_data(**kwargs)

        id_producto = self.kwargs.get('idProducto')

        context['producto'] = Estructura_Producto.objects.get(
            id=id_producto
        )

        context['estructura'] = Estructura_Producto.objects.filter(
            padre=id_producto
        ).order_by('producto')

        return context


class Generar_Estructura(LoginRequiredMixin, TemplateView):
    template_name = 'inventario/generar_estructura.html'


class Lista_Productos(ListAPIView):
    serializer_class = ProductoSerializer

    def get_queryset(self):
        kword = self.kwargs['kword']

        return Producto.objects.filter(
            categoria__nombre='PRODUCTO TERMINADO',
            codigo__icontains=kword
        )


class Lista_Componentes(ListAPIView):
    serializer_class = ProductoSerializer

    def get_queryset(self):
        kword = self.kwargs['kword']

        return Producto.objects.filter(
            categoria__nombre='COMPONENTE',
            codigo__icontains=kword
        )


class Batch_Productos(LoginRequiredMixin, TemplateView):
    template_name = 'inventario/crear/batch.html'

    def validar_producto(self, producto):
        flag = False

        if Producto.objects.filter(codigo=producto.upper()).exists():
            flag = True

        return flag

    def get_context_data(self, **kwargs):
        context = super(Batch_Productos, self).get_context_data(**kwargs)

        context['Formulario'] = BatchForm

        return context

    def post(self, request, *args, **kwargs):
        path = settings.MEDIA_ROOT + '/inventario/batch/' + \
            request.FILES['archivo'].name
        path_resp = settings.MEDIA_ROOT + '/inventario/batch/' + \
            request.FILES['archivo'].name[:-4] + '_resp.csv'

        def handle_uploaded_file(file):
            with open(path, 'wb+') as destination:
                for chunk in file.chunks():
                    destination.write(chunk)

        def validar_archivo(file):
            with open(path, 'r') as file:
                reader = csv.DictReader(
                    file, delimiter=',', quoting=csv.QUOTE_NONE)

                for row in reader:
                    row_values = []
                    for field in reader.fieldnames:
                        row_values.append(row[field])

                num = reader.line_num
                if int(num) > 1000:
                    messages.error(
                        self.request, 'El limite son 1000 registros por archivo')
                    return False
                else:
                    return True

        def execute_batch(file):

            with open(path, 'r') as file:
                reader = csv.DictReader(
                    file, delimiter=',', quoting=csv.QUOTE_NONE)

                lista_productos = []
                lista_excluidos = []

                instancia_categoria = Categoria.objects.get(
                    nombre='COMPONENTE')

                #user = self.request.user.username

                for row in reader:
                    row_values = []
                    for field in reader.fieldnames:
                        row_values.append(row[field])

                    flag = self.validar_producto(row_values[0])

                    if flag == False:
                        producto = Producto(
                            codigo=row_values[0],
                            nombre=row_values[1],
                            descripcion=row_values[2],
                            categoria=instancia_categoria
                        )
                        lista_productos.append(producto)
                    else:
                        producto = Producto(
                            codigo=row_values[0],
                            nombre=row_values[1],
                            descripcion=row_values[2],
                            categoria=instancia_categoria
                        )
                        lista_excluidos.append(producto)

                Producto.objects.bulk_create(
                    lista_productos,
                    batch_size=1000
                )

                if len(lista_excluidos) > 0:
                    with open(path_resp, 'w', newline="") as f:
                        writer = csv.writer(f)
                        writer.writerow(
                            ['codigo', 'nombre', 'descripcion', 'status'])

                        for row in lista_excluidos:
                            data = []
                            data.append(row.codigo)
                            data.append(row.nombre)
                            data.append(row.descripcion)
                            data.append('EXCLUIDO')

                            writer.writerow(data)

                    messages.info(
                        self.request, request.FILES['archivo'].name[:-4] + '_resp.csv')

                msg = 'Numero de Registros: ' + str(reader.line_num - 1) + '\n' + 'Registros Insertados: ' + str(
                    len(lista_productos)) + '\n' + 'Registros Excluidos: ' + str(len(lista_excluidos))

                messages.success(self.request, msg)

        if request.method == 'POST':
            form = BatchForm(request.POST, request.FILES)
            if form.is_valid():
                handle_uploaded_file(request.FILES['archivo'])

                if validar_archivo(request.FILES['archivo']) == False:
                    return redirect(self.request.META['HTTP_REFERER'])

                execute_batch(request.FILES['archivo'])

                return redirect(self.request.META['HTTP_REFERER'])

        else:
            form = BatchForm()


def DescargarExcel(request, archivo):
    path = settings.MEDIA_ROOT + '/batch/' + archivo

    with open(path, 'rb') as file:
        response = HttpResponse(file.read(), content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename=' + \
            os.path.basename(path)

    return response
