# Generated by Django 5.0.1 on 2024-01-27 18:26

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schoolAdmin', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='staff',
            name='employmentCode',
            field=models.CharField(max_length=10, unique=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='staff',
            name='firstname',
            field=models.CharField(max_length=15),
            preserve_default=True,
        ),
    ]
