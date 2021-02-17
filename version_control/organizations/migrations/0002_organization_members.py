# Generated by Django 3.1.5 on 2021-02-17 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('organizations', '0001_initial'),
        ('version_control', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='organization',
            name='members',
            field=models.ManyToManyField(to='version_control.AppUser'),
        ),
    ]
