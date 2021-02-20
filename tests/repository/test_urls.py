import os
from unittest import mock

import pytest
from django.urls import reverse, resolve

from tests.utils.Environment import environ
from version_control.repository.views import RepositoryListView, RepositoryDetailView, RepositoryCreateView, \
    RepositoryUpdateView, RepositoryDeleteView


@pytest.fixture(autouse=True)
def mock_env_vars():
    with mock.patch.dict(os.environ, environ):
        yield


@pytest.mark.django_db
def test_repository_list():
    url = reverse('repository-list')
    assert resolve(url).func.view_class == RepositoryListView


@pytest.mark.django_db
def test_repository_detail_view():
    url = reverse('repository-detail', args=[1])
    assert resolve(url).func.view_class == RepositoryDetailView


@pytest.mark.django_db
def test_repository_create_view():
    url = reverse('repository-create')
    assert resolve(url).func.view_class == RepositoryCreateView


@pytest.mark.django_db
def test_organization_update_view():
    url = reverse('repository-update', args=[1])
    assert resolve(url).func.view_class == RepositoryUpdateView


@pytest.mark.django_db
def test_repository_delete():
    url = reverse('repository-delete', args=[1])
    assert resolve(url).func.view_class == RepositoryDeleteView
