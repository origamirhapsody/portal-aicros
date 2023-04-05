from django.shortcuts import render
from django.views import View
from .models import *
# Create your views here.



def serviciosView(request):

    template_name = "Servicios/servicios.html"
    encabezado_servicio = Encabezado_Servicio.objects.all()
    descripcion_servicios_aicros = Descripcion_Servicios_Aicros.objects.all()
    servicio_aicros = Servicio_Aicros.objects.all()

    context = {
        
    'Encabezado_Servicio': encabezado_servicio,
    'Descripcion_Servicios_Aicros': descripcion_servicios_aicros,
    'Servicio_Aicros': servicio_aicros
    
    }

    return render(request, template_name, context)
   