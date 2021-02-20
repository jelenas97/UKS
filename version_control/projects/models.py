from django.db import models
from django.urls import reverse
from enum import Enum
from version_control.organizations.models import Organization
from version_control.repository.models import Repository
# Create your models here.

class Project(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    repository = models.ForeignKey(Repository, on_delete=models.CASCADE, null = True)
    
    def get_absolute_url(self):
        return reverse('project-detail', kwargs={'pk': self.pk}) 
    
