import os
from unittest import mock
import pytest
from tests.utils.Environment import environ
from django.urls import reverse, resolve
from version_control.tasks.views import(
    TaskDetailView,
    TaskDeleteView,
    TaskListView,
    task_create_view,
    task_update_view
)

REPOSITORY_ID = 1
PROJECT_ID = 1
TASK_ID=1

@pytest.fixture(autouse=True)
def mock_env_vars():
    with mock.patch.dict(os.environ, environ):
        yield

@pytest.mark.django_db
def test_task_list():
     url = reverse('task-list', args=[REPOSITORY_ID, PROJECT_ID])
     assert resolve(url).func.view_class == TaskListView

@pytest.mark.django_db
def test_task_detail():
     url = reverse('task-detail', args=[REPOSITORY_ID, PROJECT_ID, TASK_ID])
     assert resolve(url).func.view_class == TaskDetailView

@pytest.mark.django_db
def test_task_create_view():
     url = reverse('task-create', args=[REPOSITORY_ID, PROJECT_ID])
     assert resolve(url).func == task_create_view

@pytest.mark.django_db
def test_task_update_view():
     url = reverse('task-update', args=[REPOSITORY_ID, PROJECT_ID, TASK_ID])
     assert resolve(url).func == task_update_view

@pytest.mark.django_db
def test_task_delete():
     url = reverse('task-delete', args=[REPOSITORY_ID, PROJECT_ID, TASK_ID])
     assert resolve(url).func.view_class == TaskDeleteView