# Generated by Django 4.1.1 on 2022-11-10 23:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Documentos", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Registro_y_Certificaciones_de_Software_MICONS_Columna_1",
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
                        upload_to="Página Documentos/Registro y Certificaciones de Software MICONS/Documentos/Columna 1",
                    ),
                ),
                (
                    "ícono",
                    models.ImageField(
                        blank=True,
                        null=True,
                        upload_to="Página Documentos/Registro y Certificaciones de Software MICONS/Íconos/Columna 1",
                    ),
                ),
            ],
            options={
                "verbose_name": "Registro / Certificación de SW MICONS Columna 1",
                "verbose_name_plural": "Registro / Certificación SW MICONS Columna 1",
                "ordering": ["nombre"],
            },
        ),
        migrations.CreateModel(
            name="Registro_y_Certificaciones_de_Software_MICONS_Columna_2",
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
                        upload_to="Página Documentos/Registro y Certificaciones de Software MICONS/Documentos/Columna 2",
                    ),
                ),
                (
                    "ícono",
                    models.ImageField(
                        blank=True,
                        null=True,
                        upload_to="Página Documentos/Registro y Certificaciones de Software MICONS/Íconos/Columna 2",
                    ),
                ),
            ],
            options={
                "verbose_name": "Registro / Certificación de SW MICONS Columna 2",
                "verbose_name_plural": "Registro / Certificación SW MICONS Columna 2",
                "ordering": ["nombre"],
            },
        ),
        migrations.CreateModel(
            name="Registro_y_Certificaciones_de_Software_MICONS_Columna_3",
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
                        upload_to="Página Documentos/Registro y Certificaciones de Software MICONS/Documentos/Columna 3",
                    ),
                ),
                (
                    "ícono",
                    models.ImageField(
                        blank=True,
                        null=True,
                        upload_to="Página Documentos/Registro y Certificaciones de Software MICONS/Íconos/Columna 3",
                    ),
                ),
            ],
            options={
                "verbose_name": "Registro / Certificación de SW MICONS Columna 3",
                "verbose_name_plural": "Registro / Certificación SW MICONS Columna 3",
                "ordering": ["nombre"],
            },
        ),
    ]
