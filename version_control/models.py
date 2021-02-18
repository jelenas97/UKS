from enum import Enum

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from .enums import TaskStatus
from django.urls import reverse
from .repository.models import Repository


class AppUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField()


class Organization(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    members = models.ManyToManyField(AppUser)

    def __str__(self):
        return f'{self.name}'


class Branch(models.Model):
    name = models.CharField(max_length=50)
    repository = models.ForeignKey(Repository, on_delete=models.CASCADE)
    creator = models.ForeignKey(AppUser, on_delete=models.CASCADE)


class Commit(models.Model):
    message = models.CharField(max_length=100)
    commitedOn = models.DateTimeField(default=timezone.now)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    commitedBy = models.ForeignKey(AppUser, on_delete=models.CASCADE)
    ##changes needs to be modeled


class Milestone(models.Model):
    name = models.CharField(max_length=25)
    description = models.TextField()
    dueDate = models.DateTimeField(default=timezone.now)
    isClosed = models.BooleanField()
    repository = models.ForeignKey(Repository, on_delete=models.CASCADE)


class Task(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    assignees = models.ManyToManyField(AppUser)
    #project = models.ForeignKey(Project, on_delete=models.CASCADE)
    milestone = models.ForeignKey(Milestone, on_delete=models.CASCADE)
    # labels = models.ManyToManyField(Label)


class TaskRevision(models.Model):
    updatedOn = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=255, choices=TaskStatus.choices())
    reviser = models.ForeignKey(AppUser, on_delete=models.CASCADE)
