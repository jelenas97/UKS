from datetime import date

from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView

from version_control.models import Repository
from version_control.projects.forms import WikiCreateForm
from version_control.wiki.models import Wiki, WikiRevision


def saveWiki(request, repoId):
    repo = Repository.objects.get(id=repoId)
    form = WikiCreateForm(request.POST)

    if form.is_valid():
        wiki = Wiki.objects.create(title=form.cleaned_data['title'],
                                   content=form.cleaned_data['content'],
                                   repository_id=repo.id)
        wiki.save()

        wikiRevision = WikiRevision.objects.create(wiki_id=1, reviser_id=1)
        wikiRevision.save()

        return HttpResponseRedirect('/repository/' + str(repo.id) + '/wiki')

    return render(request, "wiki/wiki_form.html", {'form': form})


class WikiCreateView(LoginRequiredMixin, CreateView):
    model = Wiki
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.repository = get_object_or_404(Repository, id=self.kwargs['repoId'])
        return super().form_valid(form)

    def get_success_url(self):
        print(self.get_object())
        return reverse_lazy('wiki-preview', kwargs={'repoId': self.object.repository.id})


class WikiPreview(ListView):
    template_name = 'wiki/wiki_preview.html'
    context_object_name = 'wikis'

    def get_queryset(self):
        return Wiki.objects.filter(repository_id=self.kwargs['repoId'])


class WikiPagePreview(DetailView):
    template_name = 'wiki/wiki_page_preview.html'
    model = Wiki

    def get_queryset(self):
        return Wiki.objects.filter(pk=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        context = super(WikiPagePreview, self).get_context_data(**kwargs)
        context['wikis'] = Wiki.objects.filter(repository_id=self.kwargs['repoId'])
        context['wikiRevisions'] = WikiRevision.objects.filter(pk=self.kwargs['pk'])
        return context
