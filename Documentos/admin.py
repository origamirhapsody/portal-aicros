from django.contrib import admin
from .models import *

# --------------------Encabezado Documentos--------------------
admin.site.register(Encabezado_Documentos)

# --------------------Texto Documentos Rápidos--------------------
admin.site.register(Texto_Documentos_Rapidos)

# --------------------Documentos de Rápido Acceso--------------------
admin.site.register(Documentos_de_Rápido_Acceso)

# --------------------Contratos Generales--------------------
admin.site.register(Contrato_General_Columna_1)
admin.site.register(Contrato_General_Columna_2)
admin.site.register(Contrato_General_Columna_3)

# --------------------Contratos Específicos--------------------
admin.site.register(Contrato_Específico_Columna_1)
admin.site.register(Contrato_Específico_Columna_2)
admin.site.register(Contrato_Específico_Columna_3)

# --------------------Listado Productos y Servicios--------------------
admin.site.register(Listado_Productos_y_Servicios_Columna_1)
admin.site.register(Listado_Productos_y_Servicios_Columna_2)
admin.site.register(Listado_Productos_y_Servicios_Columna_3)

# --------------------Registro y Certificaciones de Software CENDA--------------------
admin.site.register(Registro_y_Certificaciones_de_Software_CENDA_Columna_1)
admin.site.register(Registro_y_Certificaciones_de_Software_CENDA_Columna_2)
admin.site.register(Registro_y_Certificaciones_de_Software_CENDA_Columna_3)

# --------------------Registro y Certificaciones de Software MICONS--------------------
admin.site.register(Registro_y_Certificaciones_de_Software_MICONS_Columna_1)
admin.site.register(Registro_y_Certificaciones_de_Software_MICONS_Columna_2)
admin.site.register(Registro_y_Certificaciones_de_Software_MICONS_Columna_3)

# --------------------Otros Documentos--------------------
admin.site.register(Otros_Documentos_Columna_1)
admin.site.register(Otros_Documentos_Columna_2)
admin.site.register(Otros_Documentos_Columna_3)