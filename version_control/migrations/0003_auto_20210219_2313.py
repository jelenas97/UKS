# Generated by Django 3.1.5 on 2021-02-19 23:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('version_control', '0002_auto_20210219_2114'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commit',
            name='commitedBy',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='version_control.appuser'),
        ),
    ]
