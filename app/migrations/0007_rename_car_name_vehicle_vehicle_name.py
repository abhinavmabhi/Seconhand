# Generated by Django 5.1.6 on 2025-02-24 07:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_vehicle_car_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='vehicle',
            old_name='car_name',
            new_name='Vehicle_name',
        ),
    ]
