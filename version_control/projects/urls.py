from django.urls import path, include
from . import views
from .forms import ProjectCreationForm
from .views import(
    ProjectDetailView,
    ProjectDeleteView,
    ProjectListView,
    project_create_view,
    project_update_view
)

urlpatterns = [
    path('project/', ProjectListView.as_view(), name='project-list'),
    path('project/<int:pk>/', ProjectDetailView.as_view(), name='project-detail'),
    path('project/new', project_create_view, name='project-create' ),
    path('project/<int:pk>/update/', project_update_view, name='project-update'),
    path('project/<int:pk>/delete/', ProjectDeleteView.as_view(), name='project-delete'), 
    path('project/<int:pk>/', include('version_control.tasks.urls')),

    ]