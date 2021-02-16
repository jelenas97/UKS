from django.shortcuts import render
from .models import Project
from version_control.models import Repository, Organization
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import get_object_or_404
from .forms import ProjectCreationForm
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)

# Create your views here.

class ProjectListView(ListView):
    template_name = 'projects/projectslist.html'
    context_object_name = 'projects'

    def get_queryset(self):
        return  Project.objects.filter(repository_id = self.kwargs['repoId'])

class ProjectDetailView(DetailView):
    model = Project

class ProjectUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Project
    fields = ['name', 'description', 'organization']

    def test_func(self):
        return True

class ProjectDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Project
    success_url = '/'

    def test_func(self):
        return True

def project_create_view(request, repoId):
    active_user = request.user.id

    if request.method =='POST':

        form= ProjectCreationForm(active_user, request.POST)

        repo = Repository.objects.get(id=repoId)
        if form.is_valid():
            #form.save()
            project = Project()
            project.name = form.cleaned_data['name']
            project.description = form.cleaned_data['description']
            project.organization = form.cleaned_data['organization']
            project.repository = repo
            project.save()
    else:
        form= ProjectCreationForm(user_id = active_user)


    context = {
        'form' : form
    }

    return render(request, "projects/project_creation_form.html", context)