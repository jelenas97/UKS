from django.urls import path, include
from . import views
from .views import (
    RepositoryListView,
    RepositoryCreateView,
    RepositoryDeleteView,
    RepositoryDetailView,
    RepositoryUpdateView
)
urlpatterns = [
    path('repository/', RepositoryListView.as_view(), name='repository-list'),
    path('repository/<int:repoId>/', views.home, name='repository-homepage'),
    path('repository/<int:pk>/details/', RepositoryDetailView.as_view(), name='repository-detail'),
    path('repository/new/', RepositoryCreateView.as_view(), name='repository-create'),
    path('repository/<int:pk>/update/', RepositoryUpdateView.as_view(), name='repository-update'),
    path('repository/<int:pk>/delete/', RepositoryDeleteView.as_view(), name='repository-delete'),

    path('repository/<int:repoId>/', include('version_control.labels.urls')),

    path('repository/<int:repoId>/', include('version_control.milestones.urls')),

]

