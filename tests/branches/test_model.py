import os
from unittest import mock

import pytest

from tests.utils.Environment import environ
from version_control.branches.models import Branch
from version_control.repository.models import Repository


@pytest.fixture(autouse=True)
def mock_env_vars():
    with mock.patch.dict(os.environ, environ):
        yield


@pytest.mark.django_db
def test_create():
    Repository.objects.create(name="Repo", isPrivate=True)

    Branch.objects.create(name="Name", repository_id=1)

    bra = Branch.objects.get(name="Name")

    assert bra.repository_id == 1


@pytest.mark.django_db
def test_update():
    Repository.objects.create(name="Repo", isPrivate=True)

    bra = Branch.objects.create(name="Name", repository_id=1)

    bra.name = "Name 2"
    bra.save()

    bra_updated = Branch.objects.get(repository_id=1)

    assert bra_updated.name == "Name 2"


@pytest.mark.django_db
def test_cascade():
    repo = Repository.objects.create(name="Repo", isPrivate=True)

    Branch.objects.create(name="Name", repository_id=1)

    repo.delete()

    with pytest.raises(Branch.DoesNotExist):
        bra = Branch.objects.get(name="Name")


@pytest.mark.django_db
def test_delete():
    Repository.objects.create(name="Repo", isPrivate=True)

    bra = Branch.objects.create(name="Name", repository_id=1)

    bra.delete()

    with pytest.raises(Branch.DoesNotExist):
        bra = Branch.objects.get(name="Name")
