import os
from unittest import mock

import pytest

from tests.utils.Environment import environ
from version_control.milestones.models import Milestone
from version_control.repository.models import Repository
from version_control.projects.models import Project
from version_control.organizations.models import Organization
from version_control.tasks.models import Task
from version_control.labels.models import Label


@pytest.fixture(autouse=True)
def mock_env_vars():
    with mock.patch.dict(os.environ, environ):
        yield


@pytest.mark.django_db
def test_create():

    Repository.objects.create(name="UKS", isPrivate=False)
    Organization.objects.create(name="Microsoft") 
    Milestone.objects.create(name="First", description="Description", repository_id=1)
    Project.objects.create(name="VersionControl", description="Description", repository_id=1, organization_id=1)
   
    Task.objects.create(title="Task CRUD", description="Description", project_id=1, milestone_id=1, status='TO_DO')
    
    t = Task.objects.get(title="Task CRUD")

    assert t.status=='TO_DO'

@pytest.mark.django_db
def test_update():
    Repository.objects.create(name="UKS", isPrivate=False)
    Organization.objects.create(name="Microsoft") 
    Milestone.objects.create(name="First", description="Description", repository_id=1)
    Project.objects.create(name="VersionControl", description="Description", repository_id=1, organization_id=1)
   
    t= Task.objects.create(title="Task CRUD", description="Description", project_id=1, milestone_id=1, status='TO_DO')
    
    t.status='IN_PROGRESS'
    t.save()

    updated_t = Task.objects.get(title="Task CRUD")

    assert updated_t.status=="IN_PROGRESS"

@pytest.mark.django_db
def test_cascade():
    Repository.objects.create(name="UKS", isPrivate=False)
    Organization.objects.create(name="Microsoft") 
    Milestone.objects.create(name="First", description="Description", repository_id=1)
    p=Project.objects.create(name="VersionControl", description="Description", repository_id=1, organization_id=1)
   
    Task.objects.create(title="Task CRUD", description="Description", project_id=1, milestone_id=1, status='TO_DO')
    p.delete()

    with pytest.raises(Task.DoesNotExist):
        p = Task.objects.get(title="Task CRUD")


@pytest.mark.django_db
def test_delete():
    Repository.objects.create(name="UKS", isPrivate=True)
    Organization.objects.create(name="Microsoft") 
    Project.objects.create(name="VersionControl", description="Description", repository_id=1, organization_id=1)
    Milestone.objects.create(name="First", description="Description", repository_id=1)
   

    t=Task.objects.create(title="Task CRUD", description="Description", project_id=1, milestone_id=1, status='TO_DO')
    t.delete()

    with pytest.raises(Task.DoesNotExist):
        t = Task.objects.get(title="Task CRUD")
