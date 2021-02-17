# Generated by Django 3.1.5 on 2021-02-17 15:57

import colorfield.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('repository', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Label',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('description', models.TextField()),
                ('color', colorfield.fields.ColorField(default='#FFFFFF', max_length=18)),
                ('repository', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='repository.repository')),
            ],
        ),
    ]
