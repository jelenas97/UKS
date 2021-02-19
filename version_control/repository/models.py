from django.db import models
from django.urls import reverse

from users.models import Profile as AppUser


class Repository(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    isPrivate = models.BooleanField()
    contributors = models.ManyToManyField(AppUser, related_name = 'contributors')
    owner = models.ForeignKey(AppUser, on_delete=models.CASCADE, related_name = 'owner', null = True)

    def get_absolute_url(self):
        return reverse('repository-detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.name