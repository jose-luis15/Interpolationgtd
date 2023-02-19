# Generated by Django 3.2.4 on 2023-02-19 18:38

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CrossPointField',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('point', django.contrib.gis.db.models.fields.PointField(blank=True, help_text='Lat/Long', null=True, srid=4326, verbose_name='Localización Entities')),
            ],
        ),
    ]