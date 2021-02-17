from django import forms

from version_control.repository.models import Repository


class FormContributors(forms.ModelForm):
    class Meta:
        model = Repository
        fields = ['contributors']

    def __init__(self, users, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['contributors'].queryset = users