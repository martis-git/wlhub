# Generated by Django 3.0.6 on 2020-09-12 16:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0024_taskstate_color'),
        ('comments', '0003_auto_20200912_1923'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='task',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='tasks.Task'),
        ),
    ]
