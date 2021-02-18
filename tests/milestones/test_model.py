import os
from unittest import mock

import pytest

from tests.utils.Environment import environ
from version_control.milestones.models import Milestone
from version_control.repository.models import Repository


@pytest.fixture(autouse=True)
def mock_env_vars():
    with mock.patch.dict(os.environ, environ):
        yield


@pytest.mark.django_db
def test_create():
    Repository.objects.create(name="Repo", isPrivate=True)

    Milestone.objects.create(name="Name", description="Description", repository_id=1)

    mil = Milestone.objects.get(name="Name")

    assert mil.is_closed is False


@pytest.mark.django_db
def test_update():
    Repository.objects.create(name="Repo", isPrivate=True)

    mil = Milestone.objects.create(name="Name", description="Description", repository_id=1)

    mil.name = "Name 2"
    mil.is_closed = True
    mil.save()

    mil_updated = Milestone.objects.get(repository_id=1)

    assert mil_updated.is_closed is True
    assert mil_updated.name == "Name 2"


@pytest.mark.django_db
def test_cascade():
    repo = Repository.objects.create(name="Repo", isPrivate=True)

    Milestone.objects.create(name="Name", description="Description", repository_id=1)

    repo.delete()

    with pytest.raises(Milestone.DoesNotExist):
        mil = Milestone.objects.get(name="Name")


@pytest.mark.django_db
def test_delete():
    Repository.objects.create(name="Repo", isPrivate=True)

    mil = Milestone.objects.create(name="Name", description="Description", repository_id=1)

    mil.delete()

    with pytest.raises(Milestone.DoesNotExist):
        mil = Milestone.objects.get(name="Name")
