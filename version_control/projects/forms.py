from version_control.projects.models import Project
from version_control.organizations.models import Organization
from django import forms
from django.urls import reverse
from django.urls import reverse_lazy

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



class ProjectUpdateForm(forms.ModelForm):
    class Meta:
       model = Project
       fields = ['name', 'description', 'organization']

    def __init__(self,user_id, pk, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['organization'].queryset = Organization.objects.filter(members__user_id__in = [user_id])

        project=Project.objects.get(id=pk)
        self.fields['name'].initial=project.name
        self.fields['description'].initial=project.description
        self.fields['organization'].initial=project.organization
