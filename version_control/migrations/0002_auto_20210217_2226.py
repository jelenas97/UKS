# Generated by Django 3.1.6 on 2021-02-17 22:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('branches', '0001_initial'),
        ('version_control', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commit',
            name='branch',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='branches.branch'),
        ),
        migrations.DeleteModel(
            name='Branch',
        ),
    ]
