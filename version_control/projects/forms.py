from version_control.projects.models import Project
from version_control.models import Organization
from django import forms
from django.urls import reverse

from version_control.wiki.models import Wiki


class ProjectCreationForm(forms.ModelForm):
    class Meta:
       model = Project
       fields = ['name', 'description', 'organization']

    def __init__(self,user_id, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['organization'].queryset = Organization.objects.filter(members__user_id__in = [user_id])


class WikiCreateForm(forms.ModelForm):
    class Meta:
       model = Wiki
       fields = ['title', 'content']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
