from django.contrib import admin
from version_control.models import Repository, AppUser
from version_control.labels.models import Label

admin.site.register(Repository)
admin.site.register(Label)
admin.site.register(AppUser)
