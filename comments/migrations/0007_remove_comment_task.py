# Generated by Django 3.0.6 on 2020-09-12 16:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0006_auto_20200912_1929'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='task',
        ),
    ]