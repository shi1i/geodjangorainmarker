# Generated by Django 5.1.2 on 2024-10-20 08:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_back', '0007_alter_image_url_alter_polygon_unique_together'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='url',
            field=models.ImageField(upload_to='fgeovisor/site_back/IMAGES'),
        ),
    ]
