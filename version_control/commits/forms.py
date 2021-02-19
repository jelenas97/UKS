from django import forms

from version_control.commits.models import Commit


class CommitsCreateForm(forms.ModelForm):
    class Meta:
       model = Commit
       fields = ['title','message']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
