# Generated by Django 3.1.5 on 2021-02-14 23:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('version_control', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='project',
        ),
        migrations.DeleteModel(
            name='Project',
        ),
    ]
