from django.db import models

# ---------------- Encabezado_Documentos -------------------------------------------------------------------------

class Encabezado_Documentos(models.Model):
    título = models.CharField(max_length=50)
    texto_1 = models.TextField()
    texto_2 = models.TextField()

    def __str__(self):
        return str(self.id)

    class Meta:
        ordering = ["id"]
        verbose_name = "Encabezado Documento"
        verbose_name_plural = "Encabezado Documento"

# ---------------- Texto_Documentos_Rapidos -------------------------------------------------------------------------

class Texto_Documentos_Rapidos(models.Model):
    título = models.CharField(max_length=50)
    texto = models.TextField()

    def __str__(self):
        return str(self.id)

    class Meta:
        ordering = ["id"]
        verbose_name = "Texto Documentos Rápidos"
        verbose_name_plural = "Texto Documentos Rápidos"

# ---------------- Documentos_de_Rápido_Acceso -------------------------------------------------------------------------

class Documentos_de_Rápido_Acceso(models.Model):
    nombre = models.CharField(max_length=500)
    documento = models.FileField(
        upload_to="Página Documentos/Documentos de Rápido Acceso/Documentos/Columna 1",
        blank=True,
        null=True,
    )
    # description = models.TextField()
    ícono = models.ImageField(
        upload_to="Página Documentos/Documentos de Rápido Acceso/Íconos/Columna 1",
        blank=True,
        null=True,
    )

    def __str__(self):
        return str(self.nombre)

    class Meta:
        ordering = ["nombre"]
        verbose_name = "Documento Rápido Acceso"
        verbose_name_plural = "Documento Rápido Acceso"

# ---------------- Contrato_General_Columna_1 -------------------------------------------------------------------------

class Contrato_General_Columna_1(models.Model):
    nombre = models.CharField(max_length=500)
    documento = models.FileField(
        upload_to="Página Documentos/Contratos Generales/Documentos/Columna 1",
        blank=True,
        null=True,
    )
    # description = models.TextField()
    ícono = models.ImageField(
        upload_to="Página Documentos/Contratos Generales/Íconos/Columna 1",
        blank=True,
        null=True,
    )

    def __str__(self):
        return str(self.nombre)

    class Meta:
        ordering = ["id"]
        verbose_name = "Ctto. General Columna 1"
        verbose_name_plural = "Ctto. General Columna 1"
        # db_table = "Productos"

# ---------------- Contrato_General_Columna_2 -------------------------------------------------------------------------

class Contrato_General_Columna_2(models.Model):
    nombre = models.CharField(max_length=500)
    documento = models.FileField(
        upload_to="Página Documentos/Contratos Generales/Documentos/Columna 2",
        blank=True,
        null=True,
    )
    # description = models.TextField()
    ícono = models.ImageField(
        upload_to="Página Documentos/Contratos Generales/Íconos/Columna 2",
        blank=True,
        null=True,
    )

    def __str__(self):
        return str(self.nombre)

    class Meta:
        ordering = ["id"]
        verbose_name = "Ctto. General Columna 2"
        verbose_name_plural = "Ctto. General Columna 2"
        # db_table = "Productos"

# ---------------- Contrato_General_Columna_3 -------------------------------------------------------------------------

class Contrato_General_Columna_3(models.Model):
    nombre = models.CharField(max_length=500)
    documento = models.FileField(
        upload_to="Página Documentos/Contratos Generales/Documentos/Columna 3",
        blank=True,
        null=True,
    )
    # description = models.TextField()
    ícono = models.ImageField(
        upload_to="Página Documentos/Contratos Generales/Íconos/Columna 3",
        blank=True,
        null=True,
    )

    def __str__(self):
        return str(self.nombre)

    class Meta:
        ordering = ["id"]
        verbose_name = "Ctto. General Columna 3"
        verbose_name_plural = "Ctto. General Columna 3"
        # db_table = "Productos"

# ---------------- Contrato_Específico_Columna_1 -------------------------------------------------------------------------

class Contrato_Específico_Columna_1(models.Model):
    nombre = models.CharField(max_length=500)
    documento = models.FileField(
        upload_to="Página Documentos/Contratos Específicos/Documentos/Columna 1",
        blank=True,
        null=True,
    )
    # description = models.TextField()
    ícono = models.ImageField(
        upload_to="Página Documentos/Contratos Específicos/Íconos/Columna 1",
        blank=True,
        null=True,
    )

    def __str__(self):
        return str(self.nombre)

    class Meta:
        ordering = ["nombre"]
        verbose_name = "Ctto. Específico Columna 1"
        verbose_name_plural = "Ctto. Específico Columna 1"
        # db_table = "Ctto. Específico Columna 1"

# ---------------- Contrato_Específico_Columna_2 -------------------------------------------------------------------------

class Contrato_Específico_Columna_2(models.Model):
    nombre = models.CharField(max_length=500)
    documento = models.FileField(
        upload_to="Página Documentos/Contratos Específicos/Documentos/Columna 2",
        blank=True,
        null=True,
    )
    # description = models.TextField()
    ícono = models.ImageField(
        upload_to="Página Documentos/Contratos Específicos/Íconos/Columna 2",
        blank=True,
        null=True,
    )

    def __str__(self):
        return str(self.nombre)

    class Meta:
        ordering = ["nombre"]
        verbose_name = "Ctto. Específico Columna 2"
        verbose_name_plural = "Ctto. Específico Columna 2"
        # db_table = "Ctto. Específico Columna 2"

# ---------------- Contrato_Específico_Columna_3 -------------------------------------------------------------------------

class Contrato_Específico_Columna_3(models.Model):
    nombre = models.CharField(max_length=500)
    documento = models.FileField(
        upload_to="Página Documentos/Contratos Específicos/Documentos/Columna 3",
        blank=True,
        null=True,
    )
    # description = models.TextField()
    ícono = models.ImageField(
        upload_to="Página Documentos/Contratos Específicos/Íconos/Columna 3",
        blank=True,
        null=True,
    )

    def __str__(self):
        return str(self.nombre)

    class Meta:
        ordering = ["nombre"]
        verbose_name = "Ctto.Específico Columna 3"
        verbose_name_plural = "Ctto. Específico Columna 3"
        # db_table = "Ctto. Específico Columna 3"

# ---------------- Listado_Productos_y_Servicios_Columna_1 -------------------------------------------------------------------------

class Listado_Productos_y_Servicios_Columna_1(models.Model):
    nombre = models.CharField(max_length=500)
    documento = models.FileField(
        upload_to="Página Documentos/Listado Productos y Servicios/Documentos/Columna 1",
        blank=True,
        null=True,
    )
    # description = models.TextField()
    ícono = models.ImageField(
        upload_to="Página Documentos/Listado Productos y Servicios/Íconos/Columna 1",
        blank=True,
        null=True,
    )

    def __str__(self):
        return str(self.nombre)

    class Meta:
        ordering = ["nombre"]
        verbose_name = "Listado Productos y Servicios Columna 1"
        verbose_name_plural = "Listado Productos y Servicios Columna 1"
        # db_table = "Listado Productos y Servicios Columna 2"

# ---------------- Listado_Productos_y_Servicios_Columna_2 -------------------------------------------------------------------------

class Listado_Productos_y_Servicios_Columna_2(models.Model):
    nombre = models.CharField(max_length=500)
    documento = models.FileField(
        upload_to="Página Documentos/Listado Productos y Servicios/Documentos/Columna 2",
        blank=True,
        null=True,
    )
    # description = models.TextField()
    ícono = models.ImageField(
        upload_to="Página Documentos/Listado Productos y Servicios/Íconos/Columna 2",
        blank=True,
        null=True,
    )

    def __str__(self):
        return str(self.nombre)

    class Meta:
        ordering = ["nombre"]
        verbose_name = "Listado Productos y Servicios Columna 2"
        verbose_name_plural = "Listado Productos y Servicios Columna 2"
        # db_table = "Listado Productos y Servicios Columna 2"

# ---------------- Listado_Productos_y_Servicios_Columna_3 -------------------------------------------------------------------------

class Listado_Productos_y_Servicios_Columna_3(models.Model):
    nombre = models.CharField(max_length=500)
    documento = models.FileField(
        upload_to="Página Documentos/Listado Productos y Servicios/Documentos/Columna 3",
        blank=True,
        null=True,
    )
    # description = models.TextField()
    ícono = models.ImageField(
        upload_to="Página Documentos/Listado Productos y Servicios/Íconos/Columna 3",
        blank=True,
        null=True,
    )

    def __str__(self):
        return str(self.nombre)

    class Meta:
        ordering = ["nombre"]
        verbose_name = "Listado Productos y Servicios Columna 3"
        verbose_name_plural = "Listado Productos y Servicios Columna 3"
        # db_table = "Listado Productos y Servicios Columna 3"

# ---------------- Registro_y_Certificaciones_de_Software_CENDA_Columna_1 -------------------------------------------------------------------------

class Registro_y_Certificaciones_de_Software_CENDA_Columna_1(models.Model):
    nombre = models.CharField(max_length=500)
    documento = models.FileField(
        upload_to="Página Documentos/Registro y Certificaciones de Software CENDA/Documentos/Columna 1",
        blank=True,
        null=True,
    )
    # description = models.TextField()
    ícono = models.ImageField(
        upload_to="Página Documentos/Registro y Certificaciones de Software CENDA/Íconos/Columna 1",
        blank=True,
        null=True,
    )

    def __str__(self):
        return str(self.nombre)

    class Meta:
        ordering = ["nombre"]
        verbose_name = "Registro / Certificación de SW CENDA Columna 1"
        verbose_name_plural = "Registro / Certificación de SW CENDA Columna 1"
        # db_table = "Registro / Certificación de Software Columna 1"

# ---------------- Registro_y_Certificaciones_de_Software_CENDA_Columna_2 -------------------------------------------------------------------------

class Registro_y_Certificaciones_de_Software_CENDA_Columna_2(models.Model):
    nombre = models.CharField(max_length=500)
    documento = models.FileField(
        upload_to="Página Documentos/Registro y Certificaciones de Software CENDA/Documentos/Columna 2",
        blank=True,
        null=True,
    )
    # description = models.TextField()
    ícono = models.ImageField(
        upload_to="Página Documentos/Registro y Certificaciones de Software CENDA/Íconos/Columna 2",
        blank=True,
        null=True,
    )

    def __str__(self):
        return str(self.nombre)

    class Meta:
        ordering = ["nombre"]
        verbose_name = "Registro / Certificación de SW CENDA Columna 2"
        verbose_name_plural = "Registro / Certificación de SW CENDA Columna 2"
        # db_table = "Registro / Certificación de SW CENDA Columna 2"

# ---------------- Registro_y_Certificaciones_de_Software_CENDA_Columna_3 -------------------------------------------------------------------------

class Registro_y_Certificaciones_de_Software_CENDA_Columna_3(models.Model):
    nombre = models.CharField(max_length=500)
    documento = models.FileField(
        upload_to="Página Documentos/Registro y Certificaciones de Software CENDA/Documentos/Columna 3",
        blank=True,
        null=True,
    )
    # description = models.TextField()
    ícono = models.ImageField(
        upload_to="Página Documentos/Registro y Certificaciones de Software CENDA/Íconos/Columna 3",
        blank=True,
        null=True,
    )

    def __str__(self):
        return str(self.nombre)

    class Meta:
        ordering = ["nombre"]
        verbose_name = "Registro / Certificación de SW CENDA Columna 3"
        verbose_name_plural = "Registro / Certificación de SW CENDA Columna 3"
        # db_table = "Registro / Certificación de SW CENDA Columna 3"

# ---------------- Registro_y_Certificaciones_de_Software_MICONS_Columna_1 -------------------------------------------------------------------------

class Registro_y_Certificaciones_de_Software_MICONS_Columna_1(models.Model):
    nombre = models.CharField(max_length=500)
    documento = models.FileField(
        upload_to="Página Documentos/Registro y Certificaciones de Software MICONS/Documentos/Columna 1",
        blank=True,
        null=True,
    )
    # description = models.TextField()
    ícono = models.ImageField(
        upload_to="Página Documentos/Registro y Certificaciones de Software MICONS/Íconos/Columna 1",
        blank=True,
        null=True,
    )

    def __str__(self):
        return str(self.nombre)

    class Meta:
        ordering = ["nombre"]
        verbose_name = "Registro / Certificación de SW MICONS Columna 1"
        verbose_name_plural = "Registro / Certificación SW MICONS Columna 1"
        # db_table = "Registro / Certificación SW MICONS Columna 1"

# ---------------- Registro_y_Certificaciones_de_Software_MICONS_Columna_2 -------------------------------------------------------------------------

class Registro_y_Certificaciones_de_Software_MICONS_Columna_2(models.Model):
    nombre = models.CharField(max_length=500)
    documento = models.FileField(
        upload_to="Página Documentos/Registro y Certificaciones de Software MICONS/Documentos/Columna 2",
        blank=True,
        null=True,
    )
    # description = models.TextField()
    ícono = models.ImageField(
        upload_to="Página Documentos/Registro y Certificaciones de Software MICONS/Íconos/Columna 2",
        blank=True,
        null=True,
    )

    def __str__(self):
        return str(self.nombre)

    class Meta:
        ordering = ["nombre"]
        verbose_name = "Registro / Certificación de SW MICONS Columna 2"
        verbose_name_plural = "Registro / Certificación SW MICONS Columna 2"
        # db_table = "Registro / Certificación SW MICONS Columna 2"

# ---------------- Registro_y_Certificaciones_de_Software_MICONS_Columna_3 -------------------------------------------------------------------------

class Registro_y_Certificaciones_de_Software_MICONS_Columna_3(models.Model):
    nombre = models.CharField(max_length=500)
    documento = models.FileField(
        upload_to="Página Documentos/Registro y Certificaciones de Software MICONS/Documentos/Columna 3",
        blank=True,
        null=True,
    )
    # description = models.TextField()
    ícono = models.ImageField(
        upload_to="Página Documentos/Registro y Certificaciones de Software MICONS/Íconos/Columna 3",
        blank=True,
        null=True,
    )

    def __str__(self):
        return str(self.nombre)

    class Meta:
        ordering = ["nombre"]
        verbose_name = "Registro / Certificación de SW MICONS Columna 3"
        verbose_name_plural = "Registro / Certificación SW MICONS Columna 3"
        # db_table = "Registro / Certificación SW MICONS Columna 3"

# ---------------- Otros_Documentos_Columna_1 -------------------------------------------------------------------------

class Otros_Documentos_Columna_1(models.Model):
    nombre = models.CharField(max_length=500)
    documento = models.FileField(
        upload_to="Página Documentos/Otros Documentos/Documentos/Columna 1",
        blank=True,
        null=True,
    )
    # description = models.TextField()
    ícono = models.ImageField(
        upload_to="Página Documentos/Otros Documentos/Íconos/Columna 1",
        blank=True,
        null=True,
    )

    def __str__(self):
        return str(self.nombre)

    class Meta:
        ordering = ["nombre"]
        verbose_name = "Otro Documento Columna 1"
        verbose_name_plural = "Otro Documento Columna 1"
        # db_table = "Otro Documento Columna 1"

# ---------------- Otros_Documentos_Columna_2 -------------------------------------------------------------------------

class Otros_Documentos_Columna_2(models.Model):
    nombre = models.CharField(max_length=500)
    documento = models.FileField(
        upload_to="Página Documentos/Otros Documentos/Documentos/Columna 2",
        blank=True,
        null=True,
    )
    # description = models.TextField()
    ícono = models.ImageField(
        upload_to="Página Documentos/Otros Documentos/Íconos/Columna 2",
        blank=True,
        null=True,
    )

    def __str__(self):
        return str(self.nombre)

    class Meta:
        ordering = ["nombre"]
        verbose_name = "Otro Documento Columna 2"
        verbose_name_plural = "Otro Documento Columna 2"
        # db_table = "Otro Documento Columna 2"

# ---------------- Otros_Documentos_Columna_3 -------------------------------------------------------------------------

class Otros_Documentos_Columna_3(models.Model):
    nombre = models.CharField(max_length=500)
    documento = models.FileField(
        upload_to="Página Documentos/Otros Documentos/Documentos/Columna 3",
        blank=True,
        null=True,
    )
    # description = models.TextField()
    ícono = models.ImageField(
        upload_to="Página Documentos/Otros Documentos/Íconos/Columna 3",
        blank=True,
        null=True,
    )

    def __str__(self):
        return str(self.nombre)

    class Meta:
        ordering = ["nombre"]
        verbose_name = "Otro Documento Columna 3"
        verbose_name_plural = "Otro Documento Columna 3"
        # db_table = "Otro Documento Columna 3"