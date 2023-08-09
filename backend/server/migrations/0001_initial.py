# Generated by Django 4.2.1 on 2023-06-09 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Customers",
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
                ("name", models.CharField(max_length=100, null=True)),
                ("contact", models.CharField(max_length=10)),
                ("address", models.CharField(max_length=250)),
                ("age", models.CharField(max_length=3)),
                ("createdAt", models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="Driver",
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
                ("name", models.CharField(max_length=100, null=True)),
                ("contact", models.CharField(max_length=10, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="Vehicle",
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
                ("vehicleid", models.CharField(max_length=100, null=True)),
                ("customerid", models.CharField(max_length=100, null=True)),
                ("driverid", models.CharField(max_length=100, null=True)),
                ("tripdate", models.CharField(max_length=100, null=True)),
                ("ttype", models.CharField(max_length=100)),
                ("pickup", models.CharField(max_length=100, null=True)),
                ("dropoff", models.CharField(max_length=100, null=True)),
                ("pickuptime", models.DateTimeField(max_length=100)),
                ("dropofftime", models.DateTimeField(max_length=100)),
                ("createdAt", models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
    ]
