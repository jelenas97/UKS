import os
from unittest import mock

import pytest
from django.contrib.auth.models import User

from tests.utils.Environment import environ
from version_control.repository.models import Repository


@pytest.fixture(autouse=True)
def mock_env_vars():
    with mock.patch.dict(os.environ, environ):
        yield


@pytest.mark.django_db
def test_create():
    user1 = User.objects.create(username="uname", first_name="Name", last_name="LName")
    user2 = User.objects.create_user(username="uname2", first_name="Name2", last_name="LName2")

    repo = Repository.objects.create(name="Name", description="Description", isPrivate=True)
    repo.contributors.add(user1.profile)
    repo.contributors.add(user2.profile)
    repo.save()

    assert len(repo.contributors.all()) == 2


@pytest.mark.django_db
def test_update():
    user1 = User.objects.create(username="uname", first_name="Name", last_name="LName")
    user2 = User.objects.create_user(username="uname2", first_name="Name2", last_name="LName2")

    repo = Repository.objects.create(name="Name", description="Description", isPrivate=False)
    repo.contributors.add(user1.profile)
    repo.contributors.add(user2.profile)
    repo.save()

    repo.contributors.remove(user1.profile)

    assert len(repo.contributors.all()) == 1


@pytest.mark.django_db
def test_delete():
    user1 = User.objects.create(username="uname", first_name="Name", last_name="LName")
    user2 = User.objects.create_user(username="uname2", first_name="Name2", last_name="LName2")

    repo = Repository.objects.create(name="Name", description="Description", isPrivate=False)
    repo.contributors.add(user1.profile)
    repo.contributors.add(user2.profile)
    repo.save()

    repo.delete()

    with pytest.raises(Repository.DoesNotExist):
        org = Repository.objects.get(name="Name")
