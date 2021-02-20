from django.contrib import admin

from version_control.branches.models import Branch
from version_control.commits.models import Commit
from version_control.projects.models import Project
from version_control.models import AppUser
from version_control.repository.models import Repository
from version_control.organizations.models import Organization
from version_control.milestones.models import Milestone
from version_control.labels.models import Label
from version_control.tasks.models import Task
from version_control.tasks.models import TaskRevision
from version_control.wiki.models import Wiki, WikiRevision


admin.site.register(Project)
admin.site.register(Repository)
admin.site.register(Label)
admin.site.register(Wiki)
admin.site.register(WikiRevision)
admin.site.register(AppUser)
admin.site.register(Organization)
admin.site.register(Milestone)
admin.site.register(Task)
admin.site.register(TaskRevision)
admin.site.register(Branch)
admin.site.register(Commit)
