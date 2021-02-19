from django.db import models
from version_control.enums import TaskStatus
from users.models import Profile
from version_control.projects.models import Project
from version_control.labels.models import Label
from django.utils import timezone
from version_control.milestones.models import Milestone

class Task(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    assignees = models.ManyToManyField(Profile)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    milestone = models.ForeignKey(Milestone, on_delete=models.CASCADE, null=True)
    labels = models.ManyToManyField(Label)
    status = models.CharField(max_length=255, choices=TaskStatus.choices())

class TaskRevision(models.Model):
    updatedOn = models.DateTimeField(default=timezone.now)
    reviser = models.ForeignKey(Profile, on_delete=models.CASCADE)
    task= models.ForeignKey(Task, on_delete=models.CASCADE )