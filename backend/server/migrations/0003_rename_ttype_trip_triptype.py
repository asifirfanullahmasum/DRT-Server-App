# Generated by Django 4.2.1 on 2023-06-09 10:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("server", "0002_customer_trip_delete_customers_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="trip",
            old_name="ttype",
            new_name="triptype",
        ),
    ]