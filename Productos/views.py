from django.shortcuts import render
from django.views import View
from .models import *
# Create your views here.


def productosView(request):
    template_name = "Productos/productos.html"
    encabezado_producto = Encabezado_Producto.objects.all()
    descripcion_productos_aicros = Descripcion_Productos_Aicros.objects.all()
    descripcion_productos_distribuidos = Descripcion_Productos_Distribuidos.objects.all()
    producto_aicros = Producto_Aicros.objects.all()
    producto_distribuido_aicros = Producto_Distribuido_Aicros.objects.all()

    context = {
        
    'Encabezado_Producto': encabezado_producto,
    'Descripcion_Productos_Aicros': descripcion_productos_aicros,
    'Descripcion_Productos_Distribuidos': descripcion_productos_distribuidos,
    'Producto_Aicros': producto_aicros,
    'Producto_Distribuido_Aicros': producto_distribuido_aicros 
    
    }
    return render(request, template_name, context)
