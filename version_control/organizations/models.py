from django.db import models
from version_control.models import AppUser
from django.urls import reverse

# Create your models here.
class Organization(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    members = models.ManyToManyField(AppUser)

    def get_absolute_url(self):
        return reverse('organization-detail', kwargs={'pk': self.pk})

    def __str__(self):
        return f'{self.name}'



