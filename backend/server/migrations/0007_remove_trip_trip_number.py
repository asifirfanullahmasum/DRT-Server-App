# Generated by Django 4.2.2 on 2023-06-30 20:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("server", "0006_trip_trip_number"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="trip",
            name="trip_number",
        ),
    ]
