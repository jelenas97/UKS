import os
from unittest import mock

import pytest
from django.contrib.auth.models import User
from django.test import Client
from django.urls import reverse

from tests.utils.Environment import environ
from version_control.organizations.models import Organization


@pytest.fixture(autouse=True)
def mock_env_vars():
    with mock.patch.dict(os.environ, environ):
        yield


@pytest.mark.django_db
def test_organizations_list_view():
    client = Client()

    response = client.get(reverse("organization-list"))

    assert response.status_code == 200
    assert "organizations/organization_list.html" in (t.name for t in response.templates)


@pytest.mark.django_db
def test_organizations_detail_view():
    client = Client()

    Organization.objects.create(name="Org")

    response = client.get(reverse("organization-detail", args=[1]))
    assert response.status_code == 200
    assert "organizations/organization_detail.html" in (t.name for t in response.templates)


@pytest.mark.django_db
def test_organization_create_view():
    user1 = User.objects.create(username="uname", first_name="Name", last_name="LName")
    client = Client()
    client.force_login(user1)

    response = client.get(reverse("organization-create"))
    assert response.status_code == 200
    assert "organizations/organization_form.html" in (t.name for t in response.templates)


@pytest.mark.django_db
def test_organizations_update_view():
    user1 = User.objects.create(username="uname", first_name="Name", last_name="LName")
    client = Client()
    client.force_login(user1)

    Organization.objects.create(name="Org")

    response = client.get(reverse("organization-update", args=[1]))
    assert response.status_code == 200
    assert "organizations/organization_form.html" in (t.name for t in response.templates)


@pytest.mark.django_db
def test_organizations_delete_view():
    user1 = User.objects.create(username="uname", first_name="Name", last_name="LName")
    client = Client()
    client.force_login(user1)

    Organization.objects.create(name="Org")

    response = client.get(reverse("organization-delete", args=[1]))
    assert response.status_code == 200
    assert "organizations/organization_confirm_delete.html" in (t.name for t in response.templates)
