from django.urls import path
from .views import (
    WikiCreateView,
    WikiPreview,
    WikiPagePreview, saveWiki

)

urlpatterns = [
    path('wiki/new', saveWiki, name='wiki-create'),
    path('wiki/<int:pk>/', WikiPagePreview.as_view(), name='wiki-page-preview'),
    path('wiki', WikiPreview.as_view(), name='wiki-preview')
]
