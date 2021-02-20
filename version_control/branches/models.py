from django.db import models
from django.urls import reverse

from version_control.repository.models import Repository


class Branch(models.Model):
    name = models.CharField(max_length=50, unique=True)
    repository = models.ForeignKey(Repository, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('branch-detail', kwargs={'repoId': self.repository.id, 'pk': self.id})
