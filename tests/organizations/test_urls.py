import os
from unittest import mock

import pytest
from django.urls import reverse, resolve

from tests.utils.Environment import environ
from version_control.organizations.views import OrganizationListView, OrganizationDetailView, OrganizationCreateView, \
    OrganizationUpdateView, OrganizationDeleteView


@pytest.fixture(autouse=True)
def mock_env_vars():
    with mock.patch.dict(os.environ, environ):
        yield


@pytest.mark.django_db
def test_organizations_list():
    url = reverse('organization-list')
    assert resolve(url).func.view_class == OrganizationListView


@pytest.mark.django_db
def test_organization_detail_view():
    url = reverse('organization-detail', args=[1])
    assert resolve(url).func.view_class == OrganizationDetailView


@pytest.mark.django_db
def test_organization_create_view():
    url = reverse('organization-create')
    assert resolve(url).func.view_class == OrganizationCreateView


@pytest.mark.django_db
def test_organization_update_view():
    url = reverse('organization-update', args=[1])
    assert resolve(url).func.view_class == OrganizationUpdateView


@pytest.mark.django_db
def test_organization_delete():
    url = reverse('organization-delete', args=[1])
    assert resolve(url).func.view_class == OrganizationDeleteView
