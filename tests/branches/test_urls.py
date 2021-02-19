import os
from unittest import mock

import pytest
from django.urls import reverse, resolve

from tests.utils.Environment import environ
from version_control.branches.views import BranchListView, BranchDetailView, BranchCreateView, BranchDeleteView, \
    BranchUpdateView


@pytest.fixture(autouse=True)
def mock_env_vars():
    with mock.patch.dict(os.environ, environ):
        yield


@pytest.mark.django_db
def test_branch_list():
    url = reverse('branch-list', args=[1])
    assert resolve(url).func.view_class == BranchListView


@pytest.mark.django_db
def test_branch_detail_view():
    url = reverse('branch-detail', args=[1])
    assert resolve(url).func.view_class == BranchDetailView


@pytest.mark.django_db
def test_branch_create_view():
    url = reverse('branch-create', args=[1])
    assert resolve(url).func.view_class == BranchCreateView


@pytest.mark.django_db
def test_branch_update_view():
    url = reverse('branch-update', args=[1, "name"])
    assert resolve(url).func.view_class == BranchUpdateView


@pytest.mark.django_db
def test_branch_delete():
    url = reverse('branch-delete', args=[1, "name"])
    assert resolve(url).func.view_class == BranchDeleteView
