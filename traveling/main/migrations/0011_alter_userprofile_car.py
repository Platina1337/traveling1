# Generated by Django 5.0.6 on 2024-07-05 14:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_remove_trip_car_userprofile_car'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='car',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.car'),
        ),
    ]
