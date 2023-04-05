from django.db import models

# ---------------- Encabezado_Servicio -------------------------------------------------------------------------

class Encabezado_Servicio(models.Model):
    título = models.CharField(max_length=50)
    texto_1 = models.TextField()
    texto_2 = models.TextField()

    def __str__(self):
        return str(self.id)

    class Meta:
        ordering = ["id"]
        verbose_name = "Encabezado Servicio"
        verbose_name_plural = "Encabezado Servicio"

# ---------------- Descripcion_Servicios_Aicros -------------------------------------------------------------------------

class Descripcion_Servicios_Aicros(models.Model):
    título = models.CharField(max_length=50)
    texto_1 = models.TextField()

    def __str__(self):
        return str(self.id)

    class Meta:
        ordering = ["id"]
        verbose_name = "Descripción Servicio Aicros"
        verbose_name_plural = "Descripción Servicio Aicros"

# ---------------- Servicio_Aicros -------------------------------------------------------------------------

class Servicio_Aicros(models.Model):
    ícono = models.ImageField(upload_to="Página Servicios/Ícono")
    descripción = models.TextField()

    def __str__(self):
        return str(self.id)

    class Meta:
        ordering = ["id"]
        verbose_name = "Servicio Aicros"
        verbose_name_plural = "Servicio Aicros"

