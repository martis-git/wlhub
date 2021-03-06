# Generated by Django 3.0.6 on 2020-05-17 23:40

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0005_auto_20200518_0119'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='updated_at',
            field=models.DateField(auto_now=True, verbose_name='Дата обновления'),
        ),
        migrations.AlterField(
            model_name='task',
            name='end_at',
            field=models.DateField(blank=True, default=datetime.datetime(2020, 5, 25, 2, 40, 25, 371520), verbose_name='Дата завершения'),
        ),
        migrations.AlterField(
            model_name='task',
            name='priority',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='tasks.TaskPriority', verbose_name='Приоритет'),
        ),
        migrations.AlterField(
            model_name='task',
            name='report_status',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='tasks.ReportStatus', verbose_name='Статус отчетности'),
        ),
        migrations.AlterField(
            model_name='task',
            name='start_at',
            field=models.DateField(blank=True, default=datetime.datetime(2020, 5, 18, 2, 40, 25, 371520), verbose_name='Дата создания'),
        ),
        migrations.AlterField(
            model_name='task',
            name='state',
            field=models.ForeignKey(blank=True, default=1, null=True, on_delete=django.db.models.deletion.SET_NULL, to='tasks.TaskState', verbose_name='Состояние'),
        ),
        migrations.AlterField(
            model_name='task',
            name='subject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tasks.Subject', verbose_name='Субъект задачи'),
        ),
    ]
