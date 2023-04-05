from django.db import models

# ---------------- Encabezado_Nosotros -------------------------------------------------------------------------

class Encabezado_Nosotros(models.Model):
    título = models.CharField(max_length=50)
    texto_1 = models.TextField()
    texto_2 = models.TextField()

    def __str__(self):
        return str(self.id)

    class Meta:
        ordering = ["id"]
        verbose_name = "Encabezado Nosotros"
        verbose_name_plural = "Encabezado Nosotros"

# ---------------- Mision_Nosotros -------------------------------------------------------------------------

class Mision_Nosotros(models.Model):
    título = models.CharField(max_length=50)
    descripción = models.TextField()

    def __str__(self):
        return str(self.id)

    class Meta:
        ordering = ["id"]
        verbose_name = "Misión"
        verbose_name_plural = "Misión"

# ---------------- Vision_Nosotros -------------------------------------------------------------------------

class Vision_Nosotros(models.Model):
    título = models.CharField(max_length=50)
    descripción = models.TextField()

    def __str__(self):
        return str(self.id)

    class Meta:
        ordering = ["id"]
        verbose_name = "Visión"
        verbose_name_plural = "Visión"

# ---------------- Valores_Nosotros -------------------------------------------------------------------------

class Valores_Nosotros(models.Model):
    título = models.CharField(max_length=50)
    descripción = models.TextField()

    def __str__(self):
        return str(self.id)

    class Meta:
        ordering = ["id"]
        verbose_name = "Valores"
        verbose_name_plural = "Valores"

# ---------------- Anno_Historia -------------------------------------------------------------------------

class Anno_Historia(models.Model):
    número = models.CharField(max_length=50)
    descripción = models.TextField()

    def __str__(self):
        return str(self.número)

    class Meta:
        ordering = ["número"]
        verbose_name = "Año de Historia"
        verbose_name_plural = "Año de Historia"

# ---------------- Miembro_de_Trabajo -------------------------------------------------------------------------

class Miembro_de_Trabajo(models.Model):
    foto = models.ImageField(
        upload_to="Página Nosotros/Miembro de Trabajo/Imágenes", blank=True, null=True
    )
    nombre = models.CharField(max_length=100)
    cargo = models.CharField(max_length=100)
    correo = models.EmailField(max_length=254)

    def __str__(self):
        return str(self.id)

    class Meta:
        ordering = ["id"]
        verbose_name = "Miembro de Trabajo"
        verbose_name_plural = "Miembro de Trabajo"

# ---------------- Eventos -------------------------------------------------------------------------

class Evento(models.Model):
    título = models.CharField(max_length=50)
    descripción = models.TextField(max_length=430)

    def __str__(self):
        return str(self.título)

    class Meta:
        ordering = ["título"]
        verbose_name = "Evento"
        verbose_name_plural = "Evento"