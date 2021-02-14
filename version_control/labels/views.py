from django.shortcuts import render
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from django.shortcuts import get_object_or_404

from .models import Label, Repository

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

class LabelUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Label
    fields = ['name', 'description', 'color']
    def test_func(self):
        return True


class LabelDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Label
    success_url = '/'

    def test_func(self):
        return True
