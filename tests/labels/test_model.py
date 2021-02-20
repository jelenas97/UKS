import os
from unittest import mock

import pytest

from tests.utils.Environment import environ
from version_control.labels.models import Label
from version_control.repository.models import Repository


@pytest.fixture(autouse=True)
def mock_env_vars():
    with mock.patch.dict(os.environ, environ):
        yield


@pytest.mark.django_db
def test_create():
    Repository.objects.create(name="Repo", isPrivate=True)

    Label.objects.create(name="Name", description="Description", repository_id=1)

    lab = Label.objects.get(name="Name")

    assert lab.color == "#FFFFFF"


@pytest.mark.django_db
def test_update():
    Repository.objects.create(name="Repo", isPrivate=True)

    lab = Label.objects.create(name="Name", description="Description", color="#12c773", repository_id=1)

    lab.name = "Name 2"
    lab.color = "#e7e3cd"
    lab.save()

    lab_updated = Label.objects.get(repository_id=1)

    assert lab_updated.color == "#e7e3cd"
    assert lab_updated.name == "Name 2"


@pytest.mark.django_db
def test_cascade():
    repo = Repository.objects.create(name="Repo", isPrivate=True)

    Label.objects.create(name="Name", description="Description", color="#12c773", repository_id=1)

    repo.delete()

    with pytest.raises(Label.DoesNotExist):
        lab = Label.objects.get(name="Name")


@pytest.mark.django_db
def test_delete():
    Repository.objects.create(name="Repo", isPrivate=True)

    lab = Label.objects.create(name="Name", description="Description", repository_id=1)

    lab.delete()

    with pytest.raises(Label.DoesNotExist):
        lab = Label.objects.get(name="Name")
