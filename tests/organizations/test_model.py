import os
from unittest import mock

import pytest
from django.contrib.auth.models import User

from tests.utils.Environment import environ
from version_control.organizations.models import Organization


@pytest.fixture(autouse=True)
def mock_env_vars():
    with mock.patch.dict(os.environ, environ):
        yield


@pytest.mark.django_db
def test_create():
    user1 = User.objects.create(username="uname", first_name="Name", last_name="LName")
    user2 = User.objects.create_user(username="uname2", first_name="Name2", last_name="LName2")

    org = Organization.objects.create(name="Name", description="Description")
    org.members.add(user1.profile)
    org.members.add(user2.profile)
    org.save()

    assert len(org.members.all()) == 2


@pytest.mark.django_db
def test_update():
    user1 = User.objects.create(username="uname", first_name="Name", last_name="LName")
    user2 = User.objects.create_user(username="uname2", first_name="Name2", last_name="LName2")

    org = Organization.objects.create(name="Name", description="Description")
    org.members.add(user1.profile)
    org.members.add(user2.profile)
    org.save()

    org.members.remove(user1.profile)

    assert len(org.members.all()) == 1


@pytest.mark.django_db
def test_delete():
    user1 = User.objects.create(username="uname", first_name="Name", last_name="LName")
    user2 = User.objects.create_user(username="uname2", first_name="Name2", last_name="LName2")

    org = Organization.objects.create(name="Name", description="Description")
    org.members.add(user1.profile)
    org.members.add(user2.profile)
    org.save()

    org.delete()

    with pytest.raises(Organization.DoesNotExist):
        org = Organization.objects.get(name="Name")
