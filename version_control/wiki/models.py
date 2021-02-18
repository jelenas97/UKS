from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

from version_control.models import Repository, AppUser


class Wiki(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    createdOn = models.DateTimeField(default=timezone.now)
    repository = models.ForeignKey(Repository, on_delete=models.CASCADE)


class WikiRevision(models.Model):
    wiki = models.ForeignKey(Wiki, on_delete=models.CASCADE)
    updatedOn = models.DateTimeField(default=timezone.now)
    reviser = models.ForeignKey(AppUser, on_delete=models.CASCADE)
