from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.views.generic import CreateView

from version_control.models import Repository
from version_control.wiki.models import Wiki


class WikiCreateView(LoginRequiredMixin, CreateView):
    model = Wiki
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.repository = get_object_or_404(Repository, id=self.kwargs['repoId'])
        return super().form_valid(form)