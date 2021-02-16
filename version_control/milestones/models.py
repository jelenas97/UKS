from django.db import models
from django.urls import reverse
from django.utils import timezone

from version_control.repository.models import Repository


class Milestone(models.Model):
    name = models.CharField(max_length=25)
    description = models.TextField()
    due_date = models.DateField(default=timezone.now)
    is_closed = models.BooleanField(default=False)
    repository = models.ForeignKey(Repository, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('milestone-detail', kwargs={'repoId': self.repository.id, 'pk': self.pk})
