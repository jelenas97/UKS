from django.contrib import admin
from version_control.projects.models import Project
from version_control.milestones.models import Milestone
from version_control.models import Repository, AppUser
from version_control.labels.models import Label


admin.site.register(Project)
admin.site.register(Repository)
admin.site.register(Label)
admin.site.register(AppUser)
admin.site.register(Milestone)
