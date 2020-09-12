# Generated by Django 3.0.6 on 2020-09-12 15:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0016_auto_20200912_1825'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='taskstate',
            name='color',
        ),
        migrations.AlterField(
            model_name='task',
            name='end_at',
            field=models.DateField(blank=True, default=datetime.datetime(2020, 9, 19, 18, 27, 12, 777188), verbose_name='Дата завершения'),
        ),
        migrations.AlterField(
            model_name='task',
            name='start_at',
            field=models.DateField(blank=True, default=datetime.datetime(2020, 9, 12, 18, 27, 12, 776190), verbose_name='Дата создания'),
        ),
    ]
