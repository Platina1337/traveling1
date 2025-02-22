# Generated by Django 5.0.6 on 2024-07-04 13:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_rename_user_userprofile'),
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=255)),
                ('model', models.CharField(max_length=255)),
                ('color', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('region', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Trip',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('departure_date', models.DateField()),
                ('departure_time', models.TimeField()),
                ('arrival_time', models.TimeField()),
                ('passengers', models.PositiveIntegerField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.car')),
                ('departure_city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='departure_city', to='main.city')),
                ('destination_city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='destination_city', to='main.city')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.userprofile')),
            ],
        ),
    ]
