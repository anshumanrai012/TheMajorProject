# Generated by Django 2.0.2 on 2018-03-04 11:12

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='CreditDetail',
            new_name='Credit',
        ),
    ]
