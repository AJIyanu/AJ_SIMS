# Generated by Django 5.0.1 on 2024-01-28 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lecturers', '0007_attendance_term_score_term_subject_term'),
        ('schoolAdmin', '0006_alter_academicsession_createda_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subject',
            name='term',
            field=models.ManyToManyField(related_name='term_subject', to='schoolAdmin.term'),
        ),
    ]
