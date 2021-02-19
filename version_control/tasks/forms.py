from version_control.projects.models import Project
from version_control.milestones.models import Milestone
from version_control.tasks.models import Task
from version_control.repository.models import Repository
from users.models import Profile
from django import forms
from django.urls import reverse
from django.urls import reverse_lazy


class TaskCreationForm(forms.ModelForm):
    class Meta:
       model = Task
       fields = ['title','description','assignees','milestone','labels']

    def __init__(self, repo_id, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['milestone'].queryset = Milestone.objects.filter(repository_id = repo_id)

        r=Repository.objects.get(id=repo_id)
        profiles=r.contributors
        self.fields['assignees'].queryset = profiles

class TaskUpdateForm(forms.ModelForm):
    class Meta:
       model = Task
       fields = ['title','description','assignees','milestone','labels', 'status']

    def __init__(self, repo_id, tk, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['milestone'].queryset = Milestone.objects.filter(repository_id =  repo_id)

        r=Repository.objects.get(id=repo_id)
        profiles=r.contributors
        self.fields['assignees'].queryset = profiles

        task=Task.objects.get(id=tk)
        self.fields['title'].initial=task.title
        self.fields['description'].initial=task.description
        self.fields['assignees'].initial=task.assignees.all()
        self.fields['milestone'].initial=task.milestone
        self.fields['labels'].initial=task.labels.all()
        self.fields['status'].initial=task.status
        
       