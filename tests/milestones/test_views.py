import os
from unittest import mock

import pytest
from django.contrib.auth.models import User
from django.test import Client
from django.urls import reverse

from tests.utils.Environment import environ
from version_control.milestones.models import Milestone
from version_control.repository.models import Repository


@pytest.fixture(autouse=True)
def mock_env_vars():
    with mock.patch.dict(os.environ, environ):
        yield


@pytest.mark.django_db
def test_milestones_list_view():
    client = Client()

    Repository.objects.create(name="Name", description="Desc", isPrivate=True)

    response = client.get(reverse("milestone-list", args=[1]))
    assert response.status_code == 200
    assert "milestones/milestone_list.html" in (t.name for t in response.templates)


@pytest.mark.django_db
def test_milestones_detail_view():
    client = Client()

    Repository.objects.create(name="Name", description="Desc", isPrivate=True)
    Milestone.objects.create(name="Mile", description="Desc", repository_id=1)

    response = client.get(reverse("milestone-detail", args=[1, 1]))
    assert response.status_code == 200
    assert "milestones/milestone_detail.html" in (t.name for t in response.templates)


@pytest.mark.django_db
def test_milestones_create_view():
    user1 = User.objects.create(username="uname", first_name="Name", last_name="LName")
    client = Client()
    client.force_login(user1)

    Repository.objects.create(name="Name", description="Desc", isPrivate=True)

    response = client.get(reverse("milestone-create", args=[1]))
    assert response.status_code == 200
    assert "milestones/milestone_form.html" in (t.name for t in response.templates)

# @pytest.mark.django_db
# def test_milestones_update_view():
#    user1 = User.objects.create(username="uname", first_name="Name", last_name="LName")
#    client = Client()
#    client.force_login(user1)
#
#    Repository.objects.create(name="Name", description="Desc", isPrivate=True)
#
#    response = client.get(reverse("milestone-update", args=[1]))
#    assert response.status_code == 200
#    assert "milestones/milestone_form.html" in (t.name for t in response.templates)


# @pytest.mark.django_db
# def test_milestones_delete_view():
#    user1 = User.objects.create(username="uname", first_name="Name", last_name="LName")
#    client = Client()
#    client.force_login(user1)
#
#    Repository.objects.create(name="Name", description="Desc", isPrivate=True)
#
#    response = client.get(reverse("milestone-delete", args=[1]))
#    assert response.status_code == 200
#    assert "milestones/milestone_confirm_delete.html" in (t.name for t in response.templates)
