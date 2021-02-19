import os
from unittest import mock

import pytest
from django.urls import reverse, resolve

from tests.utils.Environment import environ
from version_control.branches.views import BranchListView, BranchDetailView, BranchCreateView, BranchDeleteView, \
    BranchUpdateView
from version_control.milestones.views import MilestoneListView, MilestoneDetailView, MilestoneCreateView, \
    MilestoneUpdateView, MilestoneDeleteView


@pytest.fixture(autouse=True)
def mock_env_vars():
    with mock.patch.dict(os.environ, environ):
        yield


@pytest.mark.django_db
def test_milestones_list():
    url = reverse('milestone-list', args=[1])
    assert resolve(url).func.view_class == MilestoneListView


@pytest.mark.django_db
def test_milestone_detail_view():
    url = reverse('milestone-detail', args=[1])
    assert resolve(url).func.view_class == MilestoneDetailView


@pytest.mark.django_db
def test_milestone_create_view():
    url = reverse('milestone-create', args=[1])
    assert resolve(url).func.view_class == MilestoneCreateView


@pytest.mark.django_db
def test_milestone_update_view():
    url = reverse('milestone-update', args=[1, 1])
    assert resolve(url).func.view_class == MilestoneUpdateView


@pytest.mark.django_db
def test_milestone_delete():
    url = reverse('milestone-delete', args=[1, 1])
    assert resolve(url).func.view_class == MilestoneDeleteView
