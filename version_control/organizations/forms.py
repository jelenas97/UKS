from version_control.organizations.models import Organization
from version_control.models import AppUser
from django import forms
from django.urls import reverse

class OrganizationCreationForm(forms.ModelForm):
    class Meta:
       model = Organization
       fields = ['name', 'description', 'members']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['members'].queryset = AppUser.objects.all()