# Generated by Django 3.1.5 on 2021-02-19 11:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('repository', '0001_initial'),
        ('milestones', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='milestone',
            name='repository',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='repository.repository'),
        ),
    ]
