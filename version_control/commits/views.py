from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DeleteView, UpdateView

from version_control.branches.models import Branch
from version_control.commits.forms import CommitsCreateForm
from version_control.commits.models import Commit


def CommitCreateView(request, repoId, branchId):
    current_user = request.user

    if request.method == 'POST':
        form = CommitsCreateForm(request.POST)
        branch = Branch.objects.get(id=branchId)

        if form.is_valid():
            commit = Commit.objects.create(title=form.cleaned_data['title'],
                                           message=form.cleaned_data['message'],
                                           commitedBy_id=current_user.id,
                                           branch_id=branch.id)
            commit.save()

            return HttpResponseRedirect('/repository/' + str(repoId) + '/branches/' + str(branch.id) + '/commits')
    else:
        form = CommitsCreateForm()

    return render(request, "commits/commit_form.html", {'form': form})


class CommitListView(ListView):
    template_name = 'commits/commits_view.html'
    context_object_name = 'commits'

    def get_queryset(self):
        return Commit.objects.filter(branch_id=self.kwargs['branchId'])


class CommitDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    def test_func(self):
        return True

    model = Commit

    def get_success_url(self):
        branch = Branch.objects.get(id=self.object.branch.id)
        return reverse('commit-view', kwargs={'repoId': branch.repository.id, 'branchId': branch.id})


class CommitUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    def test_func(self):
        return True

    model = Commit
    fields = ['title', 'message']

    def get_success_url(self):
        branch = Branch.objects.get(id=self.object.branch.id)
        return reverse('commit-view', kwargs={'repoId': branch.repository.id, 'branchId': branch.id})



