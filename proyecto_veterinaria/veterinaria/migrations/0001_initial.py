# Generated by Django 5.0.6 on 2024-06-02 17:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Client",
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
            ],
        ),
        migrations.CreateModel(
            name="Doctor",
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
            ],
        ),
        migrations.CreateModel(
            name="User",
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
                ("name", models.CharField(max_length=100)),
                ("contact_number", models.IntegerField()),
                ("email", models.EmailField(max_length=254)),
                ("password", models.CharField(max_length=10)),
                ("type", models.SmallIntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="Vaccine",
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
                ("name", models.CharField(max_length=100)),
                ("description", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="Pet",
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
                ("name", models.CharField(max_length=100)),
                ("breed", models.CharField(max_length=40)),
                ("age", models.SmallIntegerField()),
                (
                    "client",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="veterinaria.client",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Appointment",
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
                ("datetime", models.DateTimeField()),
                ("status", models.SmallIntegerField(default=1)),
                ("details", models.TextField(null=True)),
                (
                    "client",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="veterinaria.client",
                    ),
                ),
                (
                    "doctor",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="veterinaria.doctor",
                    ),
                ),
                (
                    "pet",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="veterinaria.pet",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="PetAllergy",
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
                ("name", models.CharField(max_length=100)),
                ("description", models.CharField(max_length=100)),
                (
                    "pet",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="veterinaria.pet",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="PetDisease",
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
                ("name", models.CharField(max_length=100)),
                ("description", models.CharField(max_length=100)),
                (
                    "pet",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="veterinaria.pet",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="PetSurgery",
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
                ("datetime", models.DateTimeField()),
                ("status", models.SmallIntegerField(default=1)),
                ("name", models.CharField(max_length=100)),
                ("details", models.TextField()),
                (
                    "doctor",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="veterinaria.doctor",
                    ),
                ),
                (
                    "pet",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="veterinaria.pet",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="doctor",
            name="user",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE, to="veterinaria.user"
            ),
        ),
        migrations.AddField(
            model_name="client",
            name="user",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE, to="veterinaria.user"
            ),
        ),
        migrations.CreateModel(
            name="PetVaccine",
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
                ("dosis", models.IntegerField()),
                ("date", models.DateField()),
                (
                    "pet",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="veterinaria.pet",
                    ),
                ),
                (
                    "vaccine",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="veterinaria.vaccine",
                    ),
                ),
            ],
        ),
    ]
