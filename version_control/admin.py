from django.contrib import admin
from version_control.models import Repository, AppUser
from version_control.labels.models import Label
from version_control.wiki.models import Wiki

admin.site.register(Repository)
admin.site.register(Label)
admin.site.register(Wiki)
admin.site.register(AppUser)
