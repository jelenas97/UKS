import os
from unittest import mock

import pytest

from tests.utils.Environment import environ
from version_control.milestones.models import Milestone
from version_control.repository.models import Repository
from version_control.projects.models import Project
from version_control.organizations.models import Organization


@pytest.fixture(autouse=True)
def mock_env_vars():
    with mock.patch.dict(os.environ, environ):
        yield


@pytest.mark.django_db
def test_create():

    Repository.objects.create(name="UKS", isPrivate=False)
    Organization.objects.create(name="Microsoft")

    Project.objects.create(name="Name", description="Description", repository_id=1, organization_id=1)

    p = Project.objects.get(name="Name")

    assert p.organization_id==1


@pytest.mark.django_db
def test_update():
    Repository.objects.create(name="UKS", isPrivate=True)
    Organization.objects.create(name="Microsoft")

    p=Project.objects.create(name="Name", description="Description", repository_id=1, organization_id=1)

    p.description = "This project..."
    p.save()

    updated_p = Project.objects.get(organization_id=1)

    assert updated_p.description== "This project..."

@pytest.mark.django_db
def test_cascade():
    r = Repository.objects.create(name="UKS", isPrivate=False)

    Project.objects.create(name="VersionControl", description="Description", repository_id=1, organization_id=1)
    r.delete()

    with pytest.raises(Project.DoesNotExist):
        p = Project.objects.get(name="VersionControl")


@pytest.mark.django_db
def test_delete():
    Repository.objects.create(name="UKS", isPrivate=True)
    Organization.objects.create(name="Microsoft") 

    p=Project.objects.create(name="VersionControl", description="Description", repository_id=1, organization_id=1)
   
    p.delete()

    with pytest.raises(Project.DoesNotExist):
        p = Project.objects.get(name="VersionControl")
