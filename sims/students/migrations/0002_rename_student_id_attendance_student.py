# Generated by Django 5.0.1 on 2024-01-19 16:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='attendance',
            old_name='student_id',
            new_name='student',
        ),
    ]