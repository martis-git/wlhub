# Generated by Django 3.0.6 on 2020-09-12 14:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0011_auto_20200912_1707'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='end_at',
            field=models.DateField(blank=True, default=datetime.datetime(2020, 9, 19, 17, 14, 0, 976482), verbose_name='Дата завершения'),
        ),
        migrations.AlterField(
            model_name='task',
            name='start_at',
            field=models.DateField(blank=True, default=datetime.datetime(2020, 9, 12, 17, 14, 0, 976482), verbose_name='Дата создания'),
        ),
    ]