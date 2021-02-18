from django.urls import path
from .views import (
    WikiPreview,
    WikiPagePreview, saveWiki, WikiRevisionsPreview, WikiUpdateView

)

urlpatterns = [
    path('wiki/new', saveWiki, name='wiki-create'),
    path('wiki/<int:pk>/', WikiPagePreview.as_view(), name='wiki-page-preview'),
    path('wiki', WikiPreview.as_view(), name='wiki-preview'),
    path('wiki/<int:pk>/revisions', WikiRevisionsPreview.as_view(), name='wiki-revisions-preview'),
    path('wiki/<int:pk>/update', WikiUpdateView.as_view(), name='wiki-update'),

]
