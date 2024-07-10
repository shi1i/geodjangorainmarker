# Generated by Django 5.0.6 on 2024-07-09 18:58

import django.contrib.gis.db.models.fields
import django.contrib.gis.geos.point
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('world', '0002_remove_weatherstation_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='weatherstation',
            name='location',
            field=django.contrib.gis.db.models.fields.PointField(default=django.contrib.gis.geos.point.Point(0, 0), srid=4326),
        ),
    ]
