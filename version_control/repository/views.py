
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)

from version_control.repository.models import Repository


def home(request, repoId):
    return render(request, 'repository/repositoryhome.html', {'repoId': repoId})

class RepositoryListView(ListView):
    template_name = 'repository/repositorylist.html'
    context_object_name = 'repository'

    def get_queryset(self):
        return Repository.objects.filter(contributors__user_id__in = [self.request.user.id])

class RepositoryCreateView(LoginRequiredMixin, CreateView):
    model = Repository
    fields = ['name', 'description', 'isPrivate', 'contributors']

    def test_func(self):
        return True
    def get_success_url(self):
        return reverse_lazy('repository-list')

class RepositoryDetailView(DetailView):
    model = Repository

    def get_queryset(self):
        return Repository.objects.filter(pk = self.kwargs['pk'])


class RepositoryUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Repository
    fields = ['name', 'description', 'isPrivate', 'contributors']


    def test_func(self):
        return True

    def get_success_url(self):
        return reverse_lazy('repository-list')


class RepositoryDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Repository
    def get_success_url(self):
        return reverse_lazy('repository-list')

    def test_func(self):
        return True
