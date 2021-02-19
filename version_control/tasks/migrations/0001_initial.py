# Generated by Django 3.1.5 on 2021-02-19 11:30

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('labels', '0002_label_repository'),
        ('projects', '0002_project_repository'),
        ('milestones', '0002_milestone_repository'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('status', models.CharField(choices=[('TO_DO', 'TO_DO'), ('IN_PROGRESS', 'IN_PROGRESS'), ('IN_REVIEW', 'IN_REVIEW'), ('DONE', 'DONE'), ('ARCHIVED', 'ARCHIVED')], max_length=255)),
                ('assignees', models.ManyToManyField(to='users.Profile')),
                ('labels', models.ManyToManyField(to='labels.Label')),
                ('milestone', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='milestones.milestone')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.project')),
            ],
        ),
        migrations.CreateModel(
            name='TaskRevision',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updatedOn', models.DateTimeField(default=django.utils.timezone.now)),
                ('reviser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.profile')),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tasks.task')),
            ],
        ),
    ]
