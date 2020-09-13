# Generated by Django 3.0.6 on 2020-09-13 13:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_auto_20200913_1634'),
    ]

    operations = [
        migrations.AddField(
            model_name='usersurvey',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='survey', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь'),
        ),
    ]