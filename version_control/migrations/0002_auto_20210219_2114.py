# Generated by Django 3.1.5 on 2021-02-19 21:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
        ('version_control', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commit',
            name='commitedBy',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.profile'),
        ),
    ]