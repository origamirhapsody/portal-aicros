# Generated by Django 4.1.1 on 2022-11-11 01:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            "Documentos",
            "0002_registro_y_certificaciones_de_software_micons_columna_1_and_more",
        ),
    ]

    operations = [
        migrations.CreateModel(
            name="Registro_y_Certificaciones_de_Software_CENDA_Columna_1",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nombre", models.CharField(max_length=500)),
                (
                    "documento",
                    models.FileField(
                        blank=True,
                        null=True,
                        upload_to="Página Documentos/Registro y Certificaciones de Software CENDA/Documentos/Columna 1",
                    ),
                ),
                (
                    "ícono",
                    models.ImageField(
                        blank=True,
                        null=True,
                        upload_to="Página Documentos/Registro y Certificaciones de Software CENDA/Íconos/Columna 1",
                    ),
                ),
            ],
            options={
                "verbose_name": "Registro / Certificación de SW CENDA Columna 1",
                "verbose_name_plural": "Registro / Certificación de SW CENDA Columna 1",
                "ordering": ["nombre"],
            },
        ),
        migrations.CreateModel(
            name="Registro_y_Certificaciones_de_Software_CENDA_Columna_2",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nombre", models.CharField(max_length=500)),
                (
                    "documento",
                    models.FileField(
                        blank=True,
                        null=True,
                        upload_to="Página Documentos/Registro y Certificaciones de Software CENDA/Documentos/Columna 2",
                    ),
                ),
                (
                    "ícono",
                    models.ImageField(
                        blank=True,
                        null=True,
                        upload_to="Página Documentos/Registro y Certificaciones de Software CENDA/Íconos/Columna 2",
                    ),
                ),
            ],
            options={
                "verbose_name": "Registro / Certificación de SW CENDA Columna 2",
                "verbose_name_plural": "Registro / Certificación de SW CENDA Columna 2",
                "ordering": ["nombre"],
            },
        ),
        migrations.CreateModel(
            name="Registro_y_Certificaciones_de_Software_CENDA_Columna_3",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nombre", models.CharField(max_length=500)),
                (
                    "documento",
                    models.FileField(
                        blank=True,
                        null=True,
                        upload_to="Página Documentos/Registro y Certificaciones de Software CENDA/Documentos/Columna 3",
                    ),
                ),
                (
                    "ícono",
                    models.ImageField(
                        blank=True,
                        null=True,
                        upload_to="Página Documentos/Registro y Certificaciones de Software CENDA/Íconos/Columna 3",
                    ),
                ),
            ],
            options={
                "verbose_name": "Registro / Certificación de SW CENDA Columna 3",
                "verbose_name_plural": "Registro / Certificación de SW CENDA Columna 3",
                "ordering": ["nombre"],
            },
        ),
        migrations.DeleteModel(
            name="Registro_y_Certificaciones_de_Software_Columna_1",
        ),
        migrations.DeleteModel(
            name="Registro_y_Certificaciones_de_Software_Columna_2",
        ),
        migrations.DeleteModel(
            name="Registro_y_Certificaciones_de_Software_Columna_3",
        ),
    ]
