# Generated by Django 3.0.6 on 2020-09-12 15:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0015_auto_20200912_1813'),
    ]

    operations = [
        migrations.AddField(
            model_name='taskstate',
            name='color',
            field=models.CharField(default='0277bd', max_length=6, verbose_name='Цвет'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='task',
            name='end_at',
            field=models.DateField(blank=True, default=datetime.datetime(2020, 9, 19, 18, 25, 22, 553886), verbose_name='Дата завершения'),
        ),
        migrations.AlterField(
            model_name='task',
            name='start_at',
            field=models.DateField(blank=True, default=datetime.datetime(2020, 9, 12, 18, 25, 22, 553886), verbose_name='Дата создания'),
        ),
    ]