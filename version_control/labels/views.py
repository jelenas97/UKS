
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from django.shortcuts import get_object_or_404

from .models import Label
from ..repository.models import Repository


class LabelListView(ListView):
    template_name = 'labels/labelslist.html'
    context_object_name = 'labels'

    def get_queryset(self):
        return Label.objects.filter(repository_id = self.kwargs['repoId'])



class LabelCreateView(LoginRequiredMixin, CreateView):
    model = Label
    fields = ['name', 'description', 'color']

    def form_valid(self, form):
        form.instance.repository = get_object_or_404(Repository, id=self.kwargs['repoId'])
        return super().form_valid(form)

class LabelDetailView(DetailView):
    model = Label

    def get_queryset(self):
        return Label.objects.filter(pk = self.kwargs['pk'])


class LabelUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Label
    fields = ['name', 'description', 'color']
    def test_func(self):
        return True


class LabelDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Label
    def get_success_url(self):
        return reverse_lazy('label-list', kwargs={'repoId': self.object.repository.id})

    def test_func(self):
        return True
