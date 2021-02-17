# Generated by Django 3.1.5 on 2021-02-15 00:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Repository',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('isPrivate', models.BooleanField()),
                ('contributors', models.ManyToManyField(to='users.Profile')),
            ],
        ),
    ]