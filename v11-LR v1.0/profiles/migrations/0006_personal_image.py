# Generated by Django 2.0.2 on 2018-04-08 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0005_auto_20180312_1924'),
    ]

    operations = [
        migrations.AddField(
            model_name='personal',
            name='image',
            field=models.ImageField(blank=True, upload_to='profile_images'),
        ),
    ]