from django.contrib import admin
from version_control.projects.models import Project 
from version_control.models import AppUser
from version_control.repository.models import Repository
from version_control.labels.models import Label
from version_control.wiki.models import Wiki, WikiRevision

# Register your models here.

admin.site.register(Project)
admin.site.register(Repository)
admin.site.register(Label)
admin.site.register(Wiki)
admin.site.register(WikiRevision)
admin.site.register(AppUser)
