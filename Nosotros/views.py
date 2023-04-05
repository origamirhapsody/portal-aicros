from django.shortcuts import render
from django.views import View
from .models import *
# Create your views here.


def aboutView(request):
    template_name = "Nosotros/nosotros.html"

    encabezado_nosotros = Encabezado_Nosotros.objects.all()
    mision_nosotros = Mision_Nosotros.objects.all()
    vision_nosotros = Vision_Nosotros.objects.all()
    valores_nosotros = Valores_Nosotros.objects.all()
    anno_historia = Anno_Historia.objects.all()
    miembro_de_trabajo = Miembro_de_Trabajo.objects.all()
    evento = Evento.objects.all()

    context = {
        'Encabezado_Nosotros': encabezado_nosotros,
        'Mision_Nosotros': mision_nosotros,
        'Vision_Nosotros': vision_nosotros,
        'Valores_Nosotros': valores_nosotros,
        'Anno_Historia': anno_historia,
        'Miembro_de_Trabajo': miembro_de_trabajo,
        'Evento': evento

         }

    return render(request, template_name, context)
