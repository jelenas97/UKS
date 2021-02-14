from colorfield.fields import ColorField
from django.db import models

# Create your models here.
from django.urls import reverse

from version_control.models import Repository


class Label(models.Model):
    name = models.CharField(max_length=25)
    description = models.TextField()
    color = ColorField(default="#FFFFFF")
    repository = models.ForeignKey(Repository, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('label-detail', kwargs={'pk': self.pk})