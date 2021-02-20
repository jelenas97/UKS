import os
from unittest import mock

import pytest
from django.urls import reverse, resolve

from tests.utils.Environment import environ
from version_control.labels.views import LabelListView, LabelDetailView, LabelCreateView, LabelUpdateView, \
    LabelDeleteView


@pytest.fixture(autouse=True)
def mock_env_vars():
    with mock.patch.dict(os.environ, environ):
        yield


@pytest.mark.django_db
def test_labels_list():
    url = reverse('label-list', args=[1])
    assert resolve(url).func.view_class == LabelListView


@pytest.mark.django_db
def test_label_detail_view():
    url = reverse('label-detail', args=[1, 1])
    assert resolve(url).func.view_class == LabelDetailView


@pytest.mark.django_db
def test_label_create_view():
    url = reverse('label-create', args=[1])
    assert resolve(url).func.view_class == LabelCreateView


@pytest.mark.django_db
def test_label_update_view():
    url = reverse('label-update', args=[1, 1])
    assert resolve(url).func.view_class == LabelUpdateView


@pytest.mark.django_db
def test_label_delete():
    url = reverse('label-delete', args=[1, 1])
    assert resolve(url).func.view_class == LabelDeleteView
