from django.shortcuts import render
from django.views import View
from .models import *
# Create your views here.


from django import template
from django.template.defaultfilters import stringfilter
from django.utils.safestring import mark_safe
from django.utils.text import normalize_newlines

register = template.Library()

@register.filter()
@stringfilter
def linebreaksodt(value, autoescape=None):
    """
    Converts all newlines in a piece of plain text to XML line breaks
    (``<text:line-break />``).
    """
    autoescape = autoescape and not isinstance(value, SafeData)
    value = normalize_newlines(value)
    if autoescape:
        value = escape(value)
    return mark_safe(value.replace('\n', '<text:line-break />'))



    

def documentosView(request):
    template_name = "Documentos/documento.html"

    encabezado_documentos = Encabezado_Documentos.objects.all()

    texto_documentos_rapidos = Texto_Documentos_Rapidos.objects.all()

    documentos_de_rápido_acceso = Documentos_de_Rápido_Acceso.objects.all()

    contrato_general_columna_1 = Contrato_General_Columna_1.objects.all()
    contrato_general_columna_2 = Contrato_General_Columna_2.objects.all()
    contrato_general_columna_3 = Contrato_General_Columna_3.objects.all()

    contrato_específico_columna_1 = Contrato_Específico_Columna_1.objects.all()
    contrato_específico_columna_2 = Contrato_Específico_Columna_2.objects.all()
    contrato_específico_columna_3 = Contrato_Específico_Columna_3.objects.all()

    listado_productos_y_servicios_columna_1 = Listado_Productos_y_Servicios_Columna_1.objects.all()
    listado_productos_y_servicios_columna_2 = Listado_Productos_y_Servicios_Columna_2.objects.all()
    listado_productos_y_servicios_columna_3 = Listado_Productos_y_Servicios_Columna_3.objects.all()

    registro_y_certificaciones_de_software_CENDA_columna_1 = Registro_y_Certificaciones_de_Software_CENDA_Columna_1.objects.all()
    registro_y_certificaciones_de_software_CENDA_columna_2 = Registro_y_Certificaciones_de_Software_CENDA_Columna_2.objects.all()
    registro_y_certificaciones_de_software_CENDA_columna_3 = Registro_y_Certificaciones_de_Software_CENDA_Columna_3.objects.all()

    registro_y_certificaciones_de_software_MICONS_columna_1 = Registro_y_Certificaciones_de_Software_MICONS_Columna_1.objects.all()
    registro_y_certificaciones_de_software_MICONS_columna_2 = Registro_y_Certificaciones_de_Software_MICONS_Columna_2.objects.all()
    registro_y_certificaciones_de_software_MICONS_columna_3 = Registro_y_Certificaciones_de_Software_MICONS_Columna_3.objects.all()

    otros_documentos_columna_1 = Otros_Documentos_Columna_1.objects.all()
    otros_documentos_columna_2 = Otros_Documentos_Columna_2.objects.all()
    otros_documentos_columna_3 = Otros_Documentos_Columna_3.objects.all()

    context = {

    'Encabezado_Documentos': encabezado_documentos,
    'Texto_Documentos_Rapidos': texto_documentos_rapidos,
    'Documentos_de_Rápido_Acceso': documentos_de_rápido_acceso, 
    
    'Contrato_General_Columna_1': contrato_general_columna_1,
    'Contrato_General_Columna_2': contrato_general_columna_2,
    'Contrato_General_Columna_3': contrato_general_columna_3,

    'Contrato_Específico_Columna_1': contrato_específico_columna_1,
    'Contrato_Específico_Columna_2': contrato_específico_columna_2,
    'Contrato_Específico_Columna_3': contrato_específico_columna_3,

    'Listado_Productos_y_Servicios_Columna_1': listado_productos_y_servicios_columna_1,
    'Listado_Productos_y_Servicios_Columna_2': listado_productos_y_servicios_columna_2,
    'Listado_Productos_y_Servicios_Columna_3': listado_productos_y_servicios_columna_3,

    'Registro_y_Certificaciones_de_Software_CENDA_Columna_1': registro_y_certificaciones_de_software_CENDA_columna_1,
    'Registro_y_Certificaciones_de_Software_CENDA_Columna_2': registro_y_certificaciones_de_software_CENDA_columna_2,
    'Registro_y_Certificaciones_de_Software_CENDA_Columna_3': registro_y_certificaciones_de_software_CENDA_columna_3,

    'Registro_y_Certificaciones_de_Software_MICONS_Columna_1': registro_y_certificaciones_de_software_MICONS_columna_1,
    'Registro_y_Certificaciones_de_Software_MICONS_Columna_2': registro_y_certificaciones_de_software_MICONS_columna_2,
    'Registro_y_Certificaciones_de_Software_MICONS_Columna_3': registro_y_certificaciones_de_software_MICONS_columna_3,

    'Otros_Documentos_Columna_1': otros_documentos_columna_1,
    'Otros_Documentos_Columna_2': otros_documentos_columna_2,
    'Otros_Documentos_Columna_3': otros_documentos_columna_3

     }
    return render(request, template_name, context)
