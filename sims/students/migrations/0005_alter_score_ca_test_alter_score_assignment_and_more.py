# Generated by Django 5.0.1 on 2024-01-25 06:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0004_student_addmission_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='score',
            name='CA_Test',
            field=models.TextField(default='[]', editable=False),
        ),
        migrations.AlterField(
            model_name='score',
            name='assignment',
            field=models.TextField(default='[]', editable=False),
        ),
        migrations.AlterField(
            model_name='score',
            name='attendance',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='score',
            name='exams',
            field=models.TextField(default='[]', editable=False),
        ),
        migrations.AlterField(
            model_name='score',
            name='point',
            field=models.FloatField(default=1, editable=False),
        ),
        migrations.AlterField(
            model_name='score',
            name='total_score',
            field=models.FloatField(default=0, editable=False),
        ),
    ]
