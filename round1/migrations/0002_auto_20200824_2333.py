# Generated by Django 3.1 on 2020-08-24 18:03

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('round1', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='iD',
        ),
        migrations.AddField(
            model_name='user',
            name='iD_member',
            field=models.CharField(default=django.utils.timezone.now, max_length=20),
            preserve_default=False,
        ),
    ]