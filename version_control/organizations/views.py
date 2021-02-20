from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import get_object_or_404
from .models import Organization
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)

class OrganizationListView(ListView):
    model= Organization
    context_object_name='organizations'

    def get_queryset(self):
        return Organization.objects.filter(members__user_id__in = [self.request.user.id])

class OrganizationDetailView(DetailView):
    model = Organization

class OrganizationUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Organization
    fields = ['name', 'description', 'members']

    def test_func(self):
        return True

class OrganizationDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Organization
    success_url = '/'

    def test_func(self):
        return True

class OrganizationCreateView(LoginRequiredMixin, CreateView):
    model = Organization
    fields = ['name', 'description', 'members']

    def test_func(self):
        return True
    def get_success_url(self):
        return reverse_lazy('organization-list')
