import os
from unittest import mock

import pytest
from django.test import Client
from django.urls import reverse

from tests.utils.Environment import environ
from version_control.organizations.models import Organization
from version_control.projects.models import Project
from version_control.repository.models import Repository
from version_control.tasks.models import Task


@pytest.fixture(autouse=True)
def mock_env_vars():
    with mock.patch.dict(os.environ, environ):
        yield


@pytest.mark.django_db
def test_task_list_view():
    client = Client()

    Repository.objects.create(name="UKS", description="This repo ...", isPrivate=False)
    Organization.objects.create(name="Microsoft")
    Project.objects.create(name="VersionControl", description="Description", repository_id=1, organization_id=1)

    response = client.get(reverse('task-list', args=[1, 1]))
    assert response.status_code == 200
    assert "tasks/tasklist.html" in (t.name for t in response.templates)


@pytest.mark.django_db
def test_task_detail_view():
    client = Client()

    Repository.objects.create(name="UKS", description="This repo ...", isPrivate=False)
    Organization.objects.create(name="Microsoft")
    Project.objects.create(name="VersionControl", description="Description", repository_id=1, organization_id=1)

    response = client.get(reverse('task-detail', args=[1, 1, 1500]))
    assert response.status_code == 404


@pytest.mark.django_db
def test_task_delete_view():
    client = Client()

    Repository.objects.create(name="UKS", description="This repo ...", isPrivate=False)
    Organization.objects.create(name="Microsoft")
    Project.objects.create(name="VersionControl", description="Description", repository_id=1, organization_id=1)

    response = client.get(reverse('task-delete', args=[1, 1, 1]))
    assert response.status_code == 302


@pytest.mark.django_db
def test_task_update_view():
    client = Client()

    Repository.objects.create(name="UKS", description="This repo ...", isPrivate=False)
    Organization.objects.create(name="Microsoft")
    p = Project.objects.create(name="VersionControl", description="Description", repository_id=1, organization_id=1)

    with pytest.raises(Task.DoesNotExist): client.post(reverse('task-update', args=[1, 1, 1500]), {
        'name': "Some task",
        'description': 'Descr',
        'project': p,
        'status': 'TO_DO'
    })


@pytest.mark.django_db
def test_task_create_view():
    client = Client()

    Repository.objects.create(name="UKS", description="This repo ...", isPrivate=False)
    Organization.objects.create(name="Microsoft")
    Project.objects.create(name="VersionControl", description="Description", repository_id=1, organization_id=1)

    response = client.get(reverse('task-create', args=[1, 1]))
    assert response.status_code == 200
    assert "tasks/task_creation_form.html" in (t.name for t in response.templates)
