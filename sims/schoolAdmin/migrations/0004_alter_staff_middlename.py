# Generated by Django 5.0.1 on 2024-01-27 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schoolAdmin', '0003_remove_staff_organogram_staff_organogram'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staff',
            name='middlename',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
    ]