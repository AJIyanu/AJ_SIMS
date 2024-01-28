# Generated by Django 5.0.1 on 2024-01-28 15:23

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schoolAdmin', '0005_term'),
    ]

    operations = [
        migrations.AlterField(
            model_name='academicsession',
            name='createda_at',
            field=models.DateField(default=django.utils.timezone.now, editable=False),
        ),
        migrations.AlterField(
            model_name='academicsession',
            name='end_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='academicsession',
            name='start_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='classes',
            name='createda_at',
            field=models.DateField(default=django.utils.timezone.now, editable=False),
        ),
        migrations.AlterField(
            model_name='departments',
            name='createda_at',
            field=models.DateField(default=django.utils.timezone.now, editable=False),
        ),
        migrations.AlterField(
            model_name='organogram',
            name='createda_at',
            field=models.DateField(default=django.utils.timezone.now, editable=False),
        ),
        migrations.AlterField(
            model_name='staff',
            name='createda_at',
            field=models.DateField(default=django.utils.timezone.now, editable=False),
        ),
        migrations.AlterField(
            model_name='subject',
            name='createda_at',
            field=models.DateField(default=django.utils.timezone.now, editable=False),
        ),
        migrations.AlterField(
            model_name='term',
            name='ends',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='term',
            name='starts',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
