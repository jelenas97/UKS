from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from version_control.branches.models import Branch
from version_control.repository.models import Repository


class BranchListView(ListView):
    template_name = 'branches/branch_list.html'
    context_object_name = 'branches'

    def get_queryset(self):
        return Branch.objects.filter(repository_id=self.kwargs['repoId'])


class BranchCreateView(LoginRequiredMixin, CreateView):
    model = Branch
    fields = ['name']

    def form_valid(self, form):
        form.instance.repository = get_object_or_404(Repository, id=self.kwargs['repoId'])
        return super().form_valid(form)


class BranchDetailView(DetailView):
    model = Branch

    def get_object(self, queryset=None):
        return Branch.objects.get(id=self.kwargs['pk'])


class BranchUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    def test_func(self):
        return True

    model = Branch
    fields = ['name']


class BranchDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    def test_func(self):
        return True

    model = Branch

    def get_success_url(self):
        return reverse_lazy('branch-list', kwargs={'repoId': self.object.repository.id})
