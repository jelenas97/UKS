# Generated by Django 3.1.6 on 2021-02-20 00:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('repository', '0001_initial'),
        ('labels', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='label',
            name='repository',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='repository.repository'),
        ),
    ]
