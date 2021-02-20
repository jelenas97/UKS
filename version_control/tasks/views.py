from django.shortcuts import render, reverse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Task, TaskRevision, TaskStatus
from django.shortcuts import get_object_or_404
from version_control.repository.models import Repository
from version_control.projects.models import Project
from django.urls import reverse_lazy
from .forms import TaskCreationForm, TaskUpdateForm
from users.models import Profile
from django.contrib.auth.models import User
from django.utils import timezone
from django.http import HttpResponseRedirect
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)

class TaskDetailView(DetailView):
    model = Task

    def test_func(self):
        return True

class TaskDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Task
    success_url = '/'

    def test_func(self):
        return True

def task_table(request, repoId, pk):
    active_user = request.user.id
    repo = Repository.objects.get(id=repoId)
    project= Project.objects.get(id=pk)
    tasks= Task.objects.filter(project=project)
    taskRevisions= TaskRevision.objects.filter(task__in=tasks)

    objects={
        'user': active_user,
        'repo': repo,
        'project': project,
        'tasks': tasks,
        'taskRevisions': taskRevisions
    }

    return render(request, "tasks/task_table.html", objects)

def task_create_view(request, repoId, pk ):

    if request.method =='POST':

        form= TaskCreationForm( repoId, request.POST)
        active_user = request.user
        profile = Profile.objects.get(user=active_user)
        project = Project.objects.get(id=pk)
        if form.is_valid():
            #form.save()
            task= Task()
            task.title =  form.cleaned_data['title']
            task.description =  form.cleaned_data['description']
            task.project= project
            task.milestone = form.cleaned_data['milestone']
            task.save()
            task.assignees.set(form.cleaned_data['assignees'])
            task.labels.set(form.cleaned_data['labels'])
            task.status='TO_DO'
            task.save()

            taskRevision= TaskRevision()
            taskRevision.reviser=profile
            taskRevision.task=task
            taskRevision.save()

            form=TaskCreationForm(repo_id=repoId )
    else:
        form= TaskCreationForm(repo_id=repoId )

    context = {
        'form' : form
    }
    return render(request, "tasks/task_creation_form.html", context)

def task_update_view(request, repoId, pk, tk):

    if request.method =='POST':

        form= TaskUpdateForm( repoId, tk, request.POST)
        active_user = request.user
        profile = Profile.objects.get(user=active_user)
        project = Project.objects.get(id=pk)
        if form.is_valid():
            #form.save()

            task= Task.objects.get(id=tk)
            task.title =  form.cleaned_data['title']
            task.description =  form.cleaned_data['description']
            task.project= project
            task.milestone = form.cleaned_data['milestone']
            task.assignees.set(form.cleaned_data['assignees'])
            task.labels.set(form.cleaned_data['labels'])
            task.status= form.cleaned_data['status']
            task.save()

            taskRevision= TaskRevision()
            taskRevision.reviser=profile
            taskRevision.task=task
            taskRevision.save()

            form= TaskUpdateForm(repo_id=repoId, tk=tk )
    else:
            form= TaskUpdateForm(repo_id=repoId, tk=tk )

    context = {
        'form' : form
    }
    return render(request, "tasks/task_update_form.html", context)

class TaskListView(ListView):
    template_name = 'tasks/tasklist.html'
    context_object_name = 'tasks'

    def get_queryset(self):
        return  Task.objects.filter(project_id = self.kwargs['pk'])

class TaskRevisionListView(ListView):
    template_name = 'tasks/taskhistory.html'
    context_object_name = 'revisions'

    def get_queryset(self):
        return  TaskRevision.objects.filter(task_id = self.kwargs['tk'])