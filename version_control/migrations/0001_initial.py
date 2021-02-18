# Generated by Django 3.1.6 on 2021-02-17 10:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('repository', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AppUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='version_control.appuser')),
                ('repository', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='repository.repository')),
            ],
        ),
        migrations.CreateModel(
            name='Milestone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('description', models.TextField()),
                ('dueDate', models.DateTimeField(default=django.utils.timezone.now)),
                ('isClosed', models.BooleanField()),
                ('repository', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='repository.repository')),
            ],
        ),
        migrations.CreateModel(
            name='TaskRevision',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updatedOn', models.DateTimeField(default=django.utils.timezone.now)),
                ('status', models.CharField(choices=[('TO_DO', 'IN'), ('IN_PROGRESS', 'IN_PROGRESS'), ('IN_REVIEW', 'IN_REVIEW'), ('DONE', 'DONE'), ('ARCHIVED', 'ARCHIVED')], max_length=255)),
                ('reviser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='version_control.appuser')),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('assignees', models.ManyToManyField(to='version_control.AppUser')),
                ('milestone', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='version_control.milestone')),
            ],
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('members', models.ManyToManyField(to='version_control.AppUser')),
            ],
        ),
        migrations.CreateModel(
            name='Commit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(max_length=100)),
                ('commitedOn', models.DateTimeField(default=django.utils.timezone.now)),
                ('branch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='version_control.branch')),
                ('commitedBy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='version_control.appuser')),
            ],
        ),
    ]
