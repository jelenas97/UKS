from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import get_object_or_404
from .models import Organization
from .forms import OrganizationCreationForm
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

def organization_create_view(request):

    if request.method =='POST':
        form= OrganizationCreationForm(request.POST)
        if form.is_valid:
            #form.save()
            organization= Organization()
            organization.name=form.cleaned_data['name']
            organization.description= form.cleaned_data['description']
            organization.members = form.cleaned_data['members']
            organization.save()
            form= OrganizationCreationForm()
    else:
        form= OrganizationCreationForm()
    context = {
        'form' : form
    }
    return render(request, "organizations/organization_creation_form.html", context)
