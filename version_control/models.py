from enum import Enum

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from colorfield.fields import ColorField
from .branches.models import Branch
from .enums import TaskStatus
from .milestones.models import Milestone
from django.urls import reverse
from .repository.models import Repository


class AppUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField()
    
    def __str__(self):
        return self.user.username

class Wiki(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    createdOn = models.DateTimeField(default=timezone.now)
    repository = models.ForeignKey(Repository, on_delete=models.CASCADE)


class WikiRevision(models.Model):
    wiki = models.ForeignKey(Wiki, on_delete=models.CASCADE)
    updatedOn = models.DateTimeField(default=timezone.now)
    reviser = models.ForeignKey(AppUser, on_delete=models.CASCADE)


class Commit(models.Model):
    message = models.CharField(max_length=100)
    commitedOn = models.DateTimeField(default=timezone.now)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    commitedBy = models.ForeignKey(AppUser, on_delete=models.CASCADE)
    # changes needs to be modeled
