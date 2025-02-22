# Generated by Django 5.0.6 on 2024-07-05 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_alter_trip_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='trip',
            name='max_passengers',
            field=models.PositiveIntegerField(default=4),
        ),
        migrations.RemoveField(
            model_name='trip',
            name='passengers',
        ),
        migrations.AddField(
            model_name='trip',
            name='passengers',
            field=models.ManyToManyField(blank=True, related_name='trip_passengers', to='main.userprofile'),
        ),
    ]
