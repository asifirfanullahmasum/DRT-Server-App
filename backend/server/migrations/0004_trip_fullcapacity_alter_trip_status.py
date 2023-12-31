# Generated by Django 4.2.1 on 2023-06-09 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("server", "0003_rename_ttype_trip_triptype"),
    ]

    operations = [
        migrations.AddField(
            model_name="trip",
            name="fullcapacity",
            field=models.CharField(
                choices=[(True, True), (False, False)], max_length=100, null=True
            ),
        ),
        migrations.AlterField(
            model_name="trip",
            name="status",
            field=models.CharField(
                choices=[("Ongoing", "Ongoing"), ("Complete", "Complete")],
                max_length=100,
                null=True,
            ),
        ),
    ]
