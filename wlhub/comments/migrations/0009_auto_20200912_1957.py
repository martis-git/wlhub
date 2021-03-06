# Generated by Django 3.0.6 on 2020-09-12 16:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0024_taskstate_color'),
        ('comments', '0008_comment_task'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='task',
        ),
        migrations.AddField(
            model_name='comment',
            name='task',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='tasks.Task', verbose_name='Связанная задача'),
            preserve_default=False,
        ),
    ]
