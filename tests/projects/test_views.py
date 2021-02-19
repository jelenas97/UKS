import os
from unittest import mock

import pytest
from django.contrib.auth.models import User
from django.test import Client
from django.urls import reverse

from tests.utils.Environment import environ
from version_control.organizations.models import Organization
from version_control.projects.models import Project
from version_control.repository.models import Repository


@pytest.fixture(autouse=True)
def mock_env_vars():
    with mock.patch.dict(os.environ, environ):
        yield


@pytest.mark.django_db
def test_project_list_view():
    client = Client()

    Repository.objects.create(name="UKS", description="This repo ...", isPrivate=False)

    response = client.get(reverse('project-list', args=[1]))
    assert response.status_code == 200
    assert "projects/projectslist.html" in (t.name for t in response.templates)


@pytest.mark.django_db
def test_project_detail_view():
    client = Client()

    Repository.objects.create(name="UKS", description="This repo ...", isPrivate=False)

    response = client.get(reverse('project-detail', args=[1, 1500]))
    assert response.status_code == 404


@pytest.mark.django_db
def test_project_create_view():
    client = Client()
    user = User.objects.create(username='user1')

    client.force_login(user)

    r = Repository.objects.create(name="UKS", isPrivate=False)
    o = Organization.objects.create(name="Microsoft")
    response = client.post(reverse('project-create', args=[1]), {
        'name': "Name", 'description': "Description", 'organization_id': o.id, 'repository_id': r.id
    })

    assert response.status_code == 200
