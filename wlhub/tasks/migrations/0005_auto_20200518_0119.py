# Generated by Django 3.0.6 on 2020-05-17 22:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0004_auto_20200518_0118'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='end_at',
            field=models.DateField(blank=True, default=datetime.datetime(2020, 5, 25, 1, 19, 50, 699408), verbose_name='Дата завершения'),
        ),
        migrations.AlterField(
            model_name='task',
            name='start_at',
            field=models.DateField(blank=True, default=datetime.datetime(2020, 5, 18, 1, 19, 50, 699408), verbose_name='Дата создания'),
        ),
    ]
