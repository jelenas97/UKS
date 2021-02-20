import os
from unittest import mock

import pytest
from django.contrib.auth.models import User
from django.test import Client
from django.urls import reverse

from tests.utils.Environment import environ
from version_control.repository.models import Repository


@pytest.fixture(autouse=True)
def mock_env_vars():
    with mock.patch.dict(os.environ, environ):
        yield


@pytest.mark.django_db
def test_repository_list_view():
    client = Client()

    response = client.get(reverse("repository-list"))

    assert response.status_code == 200
    assert "repository/repositorylist.html" in (t.name for t in response.templates)


@pytest.mark.django_db
def test_repository_detail_view():
    client = Client()

    Repository.objects.create(name="Repo", isPrivate=True)

    response = client.get(reverse("repository-detail", args=[1]))
    assert response.status_code == 200
    assert "repository/repository_detail.html" in (t.name for t in response.templates)


@pytest.mark.django_db
def test_repository_create_view():
    user1 = User.objects.create(username="uname", first_name="Name", last_name="LName")
    client = Client()
    client.force_login(user1)

    response = client.get(reverse("repository-create"))
    assert response.status_code == 200
    assert "repository/repository_form.html" in (t.name for t in response.templates)


@pytest.mark.django_db
def test_repository_update_view():
    user1 = User.objects.create(username="uname", first_name="Name", last_name="LName")
    client = Client()
    client.force_login(user1)

    Repository.objects.create(name="Repo", isPrivate=True)

    response = client.get(reverse("repository-update", args=[1]))
    assert response.status_code == 200
    assert "repository/repository_form.html" in (t.name for t in response.templates)


@pytest.mark.django_db
def test_repository_delete_view():
    user1 = User.objects.create(username="uname", first_name="Name", last_name="LName")
    client = Client()
    client.force_login(user1)

    Repository.objects.create(name="Repo", isPrivate=True)

    response = client.get(reverse("repository-delete", args=[1]))
    assert response.status_code == 200
    assert "repository/repository_confirm_delete.html" in (t.name for t in response.templates)
