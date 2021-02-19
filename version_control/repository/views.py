
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)

from users.models import Profile
from version_control.repository.forms import FormContributors
from version_control.repository.models import Repository

from ghapi.core import GhApi

def home(request, repoId):
    return render(request, 'repository/repositoryhome.html', {'repoId': repoId})

class RepositoryListView(ListView):
    template_name = 'repository/repositorylist.html'
    context_object_name = 'repository'

    def get_queryset(self):
        return Repository.objects.filter(contributors__user_id__in = [self.request.user.id])

class RepositoryCreateView(LoginRequiredMixin, CreateView):
    model = Repository
    fields = ['name', 'description', 'isPrivate']

    def test_func(self):
        return True
    def get_success_url(self):
        user = Profile.objects.get(user__username=self.request.user.username)
        self.object.owner = user
        self.object.contributors.add(user)
        self.object.save()
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

def contributors_list_add(request, repoId):
    repository = Repository.objects.get(id=repoId)
    owner = repository.owner.user.username
    users = Profile.objects.filter().exclude(user_id__in=repository.contributors.values_list('id', flat=True))
    contributors = repository.contributors.all()
    if request.method == 'POST':
        form = FormContributors(users,request.POST)
        if form.is_valid():
            users = form.data.getlist('contributors')
            for u in users:
                user = Profile.objects.get(user_id=u)
                Repository.objects.get(id=repoId).contributors.add(user)

    else:
        form = FormContributors(users = users)


    context = {'form': form, 'users': users, 'contributors': contributors, 'owner' : owner}
    return render(request, 'repository/contributors_list.html', context)


class ContributorDeleteView(LoginRequiredMixin, DeleteView):
    model = Profile
    template_name = "repository/remove_contributor.html"

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        contributor = Profile.objects.get(user_id=self.object.id)
        repository = Repository.objects.get(id=self.kwargs['repoId'])
        repository.contributors.remove(contributor)
        success_url = reverse_lazy('repository-homepage', kwargs={'repoId': self.kwargs['repoId']})
        return redirect(success_url)


def get_real_github_data(request, repoId):
    repository = Repository.objects.get(id=repoId)
    api = GhApi(owner='jelenas97',name='UKS',repo='UKS')
    branches = api.repos.list_branches(per_page=100)
    stats = api.repos.get_contributors_stats()
    for stat in stats:
        print(stat)

    context = {'branches' : branches}
    return render(request, 'repository/real_github_data.html', context)

def get_commits_from_branch(request, repoId, branch):
    repository = Repository.objects.get(id=repoId)
    api = GhApi(owner='jelenas97',name='UKS',repo='UKS')
    commits = api.repos.list_commits(sha=branch, per_page=40)
    for commit in commits:
        print(commit)


    context = {'commits' : commits}
    return render(request, 'repository/commits_from_branch.html', context)