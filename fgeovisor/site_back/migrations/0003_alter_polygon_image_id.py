# Generated by Django 5.0.7 on 2024-10-16 15:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_back', '0002_polygon_image_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='polygon',
            name='image_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='site_back.image', verbose_name='img_id'),
        ),
    ]
