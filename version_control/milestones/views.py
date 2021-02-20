from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from version_control.milestones.models import Milestone
from version_control.repository.models import Repository


class MilestoneListView(ListView):
    template_name = 'milestones/milestone_list.html'
    context_object_name = 'milestones'

    def get_queryset(self):
        return Milestone.objects.filter(repository_id=self.kwargs['repoId'])


class MilestoneCreateView(LoginRequiredMixin, CreateView):
    model = Milestone
    fields = ['name', 'description', 'due_date']

    def form_valid(self, form):
        form.instance.repository = get_object_or_404(Repository, id=self.kwargs['repoId'])
        return super().form_valid(form)


class MilestoneDetailView(DetailView):
    model = Milestone

    def get_queryset(self):
        return Milestone.objects.filter(pk=self.kwargs['pk'])


class MilestoneUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    def test_func(self):
        return True

    model = Milestone
    fields = ['name', 'description', 'due_date']


class MilestoneDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    def test_func(self):
        return True

    model = Milestone

    def get_success_url(self):
        return reverse_lazy('milestone-list', kwargs={'repoId': self.object.repository.id})
