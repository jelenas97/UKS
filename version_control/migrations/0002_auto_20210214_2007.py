# Generated by Django 3.1.5 on 2021-02-14 20:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('version_control', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='labels',
        ),
        migrations.DeleteModel(
            name='Label',
        ),
    ]