from django.urls import path
from . import views
from .forms import ProjectCreationForm
from .views import(
    ProjectDetailView,
    ProjectDeleteView,
    ProjectUpdateView,
    ProjectListView,
    project_create_view
)

urlpatterns = [
    path('repository/<int:repoId>/project/', ProjectListView.as_view(), name='project-list'),
    path('project/<int:pk>/', ProjectDetailView.as_view(), name='project-detail'),
    path('repository/<int:repoId>/project/new', project_create_view, name='project-create' ),
    path('project/<int:pk>/update/', ProjectUpdateView.as_view(), name='project-update'),
    path('project/<int:pk>/delete/', ProjectDeleteView.as_view(), name='project-delete'),
    ]