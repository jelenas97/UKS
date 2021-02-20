from colorfield.fields import ColorField
from django.db import models

# Create your models here.
from django.urls import reverse

from version_control.repository.models import Repository


class Label(models.Model):
    name = models.CharField(max_length=25)
    description = models.TextField()
    color = ColorField(default="#FFFFFF")
    repository = models.ForeignKey(Repository, on_delete=models.CASCADE, null = True)

    def get_absolute_url(self):
        return reverse('label-detail', kwargs={'repoId': self.repository.id, 'pk': self.pk})

    def __str__(self):
        return f'{self.name}'