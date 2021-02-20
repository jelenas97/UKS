from enum import Enum

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from colorfield.fields import ColorField
from .enums import TaskStatus
from django.urls import reverse
from .repository.models import Repository


class AppUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField()

