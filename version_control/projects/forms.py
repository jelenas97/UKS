from version_control.projects.models import Project
from version_control.models import Organization, Repository
from django import forms
from django.urls import reverse

class ProjectCreationForm(forms.ModelForm):
    class Meta:
       model = Project
       fields = ['name', 'description', 'organization']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['organization'].queryset = Organization.objects.all().filter(members=args[1])