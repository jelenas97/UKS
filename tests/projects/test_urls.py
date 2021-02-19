import os
from unittest import mock
import pytest
from tests.utils.Environment import environ
from django.urls import reverse, resolve
from version_control.projects.views import(
    ProjectDetailView,
    ProjectDeleteView,
    ProjectListView,
    project_create_view,
    project_update_view
)

REPOSITORY_ID = 1
PROJECT_ID = 1

@pytest.fixture(autouse=True)
def mock_env_vars():
    with mock.patch.dict(os.environ, environ):
        yield

@pytest.mark.django_db
def test_project_list():
     url = reverse('project-list', args=[REPOSITORY_ID])
     assert resolve(url).func.view_class == ProjectListView

@pytest.mark.django_db
def test_project_detail():
     url = reverse('project-detail', args=[REPOSITORY_ID, PROJECT_ID])
     assert resolve(url).func.view_class == ProjectDetailView

@pytest.mark.django_db
def test_project_create_view():
     url = reverse('project-create', args=[REPOSITORY_ID])
     assert resolve(url).func == project_create_view

@pytest.mark.django_db
def test_project_update_view():
     url = reverse('project-update', args=[REPOSITORY_ID, PROJECT_ID])
     assert resolve(url).func == project_update_view

@pytest.mark.django_db
def test_project_delete():
     url = reverse('project-delete', args=[REPOSITORY_ID, PROJECT_ID])
     assert resolve(url).func.view_class == ProjectDeleteView