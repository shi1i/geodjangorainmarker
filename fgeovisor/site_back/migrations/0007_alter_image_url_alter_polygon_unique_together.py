# Generated by Django 5.0.7 on 2024-10-18 17:47

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_back', '0006_rename_user_activitylog_login_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='url',
            field=models.ImageField(upload_to='site_back/IMAGES'),
        ),
        migrations.AlterUniqueTogether(
            name='polygon',
            unique_together={('login', 'polygon_data')},
        ),
    ]
