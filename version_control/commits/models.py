from django.db import models
from django.urls import reverse
from django.utils import timezone

from users.models import Profile
from version_control.branches.models import Branch


class Commit(models.Model):
    title = models.CharField(max_length=50)
    message = models.CharField(max_length=100)
    commitedOn = models.DateTimeField(default=timezone.now)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    commitedBy = models.ForeignKey(Profile, on_delete=models.CASCADE)

