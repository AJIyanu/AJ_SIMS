# Generated by Django 5.0.1 on 2024-01-29 08:11

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('students', '0005_grade_term'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='guardian',
            name='permission',
            field=models.ManyToManyField(related_name='guardian_user', to='auth.permission'),
        ),
        migrations.AddField(
            model_name='guardian',
            name='user_login',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]