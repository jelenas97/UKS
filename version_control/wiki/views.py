from datetime import date

from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, UpdateView

from version_control.models import Repository
from version_control.projects.forms import WikiCreateForm
from version_control.wiki.models import Wiki, WikiRevision


def saveWiki(request, repoId):
    repo = Repository.objects.get(id=repoId)

    if request.method == 'POST':
        form = WikiCreateForm(request.POST)

        if form.is_valid():
            wiki = Wiki.objects.create(title=form.cleaned_data['title'],
                                       content=form.cleaned_data['content'],
                                       repository_id=repo.id)
            wiki.save()
            wikiRevision = WikiRevision.objects.create(wiki_id=wiki.id, reviser_id=request.user.id)
            wikiRevision.save()

            return HttpResponseRedirect('/repository/' + str(repo.id) + '/wiki')
    else:
        form = WikiCreateForm()

    return render(request, "wiki/wiki_form.html", {'form': form})


class WikiUpdateView(LoginRequiredMixin, UpdateView):
    model = Wiki
    fields = ['title', 'content']
    template_name = 'wiki/wiki_update.html'

    def form_valid(self, form):
        if form.is_valid():
            wiki = Wiki.objects.get(id=self.kwargs['pk'])
            wikiRevision = WikiRevision.objects.create(wiki_id=wiki.id, reviser_id=self.request.user.id)
            wikiRevision.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('wiki-page-preview', kwargs={'repoId': self.object.repository.id, 'pk': self.kwargs['pk']})


class WikiPreview(ListView):
    template_name = 'wiki/wiki_preview.html'
    context_object_name = 'wikis'

    def get_queryset(self):
        return Wiki.objects.filter(repository_id=self.kwargs['repoId'])

    def get_context_data(self, **kwargs):
        context = super(WikiPreview, self).get_context_data(**kwargs)
        allWikis = Wiki.objects.filter(repository_id=self.kwargs['repoId'])
        if len(allWikis) != 0:
            context['wikiRevisions'] = WikiRevision.objects.filter(wiki_id=allWikis[0].id)
        return context


class WikiRevisionsPreview(ListView):
    template_name = 'wiki/wiki_revisions_preview.html'
    context_object_name = 'wikiRevisions'

    def get_queryset(self):
        return WikiRevision.objects.filter(wiki_id=self.kwargs['pk'])


class WikiPagePreview(DetailView):
    template_name = 'wiki/wiki_page_preview.html'
    model = Wiki

    def get_queryset(self):
        return Wiki.objects.filter(pk=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        context = super(WikiPagePreview, self).get_context_data(**kwargs)
        context['wikis'] = Wiki.objects.filter(repository_id=self.kwargs['repoId'])
        context['wikiRevisions'] = WikiRevision.objects.filter(wiki_id=self.kwargs['pk'])
        return context
