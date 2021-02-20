from django.urls import path, include

from version_control.commits.views import CommitCreateView, CommitListView, CommitDeleteView, CommitUpdateView

urlpatterns = [
    path('commit/new', CommitCreateView, name='commit-create'),
    path('commits', CommitListView.as_view(), name='commit-view'),
    path('commits/<int:pk>/delete/', CommitDeleteView.as_view(), name='commits-delete'),
    path('commits/<int:pk>/update/', CommitUpdateView.as_view(), name='commits-update'),
]