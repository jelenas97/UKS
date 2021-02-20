import os
from unittest import mock

import pytest
from django.contrib.auth.models import User
from django.test import Client
from django.urls import reverse

from tests.utils.Environment import environ
from version_control.labels.models import Label
from version_control.repository.models import Repository


@pytest.fixture(autouse=True)
def mock_env_vars():
    with mock.patch.dict(os.environ, environ):
        yield


@pytest.mark.django_db
def test_labels_list_view():
    client = Client()

    Repository.objects.create(name="Name", description="Desc", isPrivate=True)

    response = client.get(reverse("label-list", args=[1]))
    assert response.status_code == 200
    assert "labels/labelslist.html" in (t.name for t in response.templates)


@pytest.mark.django_db
def test_labels_detail_view():
    client = Client()

    Repository.objects.create(name="Name", description="Desc", isPrivate=True)
    Label.objects.create(name="Label", repository_id=1)

    response = client.get(reverse("label-detail", args=[1, 1]))
    assert response.status_code == 200
    assert "labels/label_detail.html" in (t.name for t in response.templates)


@pytest.mark.django_db
def test_labels_create_view():
    user1 = User.objects.create(username="uname", first_name="Name", last_name="LName")
    client = Client()
    client.force_login(user1)

    Repository.objects.create(name="Name", description="Desc", isPrivate=True)

    response = client.get(reverse("label-create", args=[1]))
    assert response.status_code == 200
    assert "labels/label_form.html" in (t.name for t in response.templates)

@pytest.mark.django_db
def test_labels_update_view():
    user1 = User.objects.create(username="uname", first_name="Name", last_name="LName")
    client = Client()
    client.force_login(user1)

    Repository.objects.create(name="Name", description="Desc", isPrivate=True)
    Label.objects.create(name="test", repository_id=1)

    response = client.get(reverse("label-update", args=[1, 1]))
    assert response.status_code == 200
    assert "labels/label_form.html" in (t.name for t in response.templates)


@pytest.mark.django_db
def test_labels_delete_view():
    user1 = User.objects.create(username="uname", first_name="Name", last_name="LName")
    client = Client()
    client.force_login(user1)

    Repository.objects.create(name="Name", description="Desc", isPrivate=True)
    Label.objects.create(name="test", repository_id=1)

    response = client.get(reverse("label-delete", args=[1, 1]))
    assert response.status_code == 200
    assert "labels/label_confirm_delete.html" in (t.name for t in response.templates)
