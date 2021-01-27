from enum import Enum

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from colorfield.fields import ColorField
from .enums import TaskStatus

class AppUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField()

class Organization(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    members = models.ManyToManyField(AppUser)

class Repository(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    isPrivate = models.BooleanField()
    contributors = models.ManyToManyField(AppUser)


class Project(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    repository = models.ForeignKey(Repository, on_delete=models.CASCADE)

class Wiki(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    createdOn = models.DateTimeField(default= timezone.now)
    repository = models.ForeignKey(Repository, on_delete=models.CASCADE)

class WikiRevision(models.Model):
    wiki = models.ForeignKey(Wiki, on_delete=models.CASCADE)
    updatedOn = models.DateTimeField(default=timezone.now)
    reviser = models.ForeignKey(AppUser, on_delete=models.CASCADE)

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
    name = models.CharField(max_length= 25)
    description = models.TextField()
    dueDate = models.DateTimeField(default=timezone.now)
    isClosed = models.BooleanField()
    repository = models.ForeignKey(Repository, on_delete=models.CASCADE)

class Label(models.Model):
    name = models.CharField(max_length=25)
    description = models.TextField()
    color = ColorField(default="#FFFFFF")
    repository = models.ForeignKey(Repository, on_delete=models.CASCADE)


class Task(models.Model):
    title = models.CharField(max_length = 50)
    description = models.TextField()
    assignees = models.ManyToManyField(AppUser)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    milestone = models.ForeignKey(Milestone, on_delete=models.CASCADE)
    labels = models.ManyToManyField(Label)

class TaskRevision(models.Model):
    updatedOn = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=255, choices=TaskStatus.choices())
    reviser = models.ForeignKey(AppUser, on_delete=models.CASCADE)



