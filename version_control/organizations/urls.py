from django.urls import path
from . import views
from .forms import OrganizationCreationForm
from .views import(
    OrganizationDetailView,
    OrganizationDeleteView,
    OrganizationUpdateView,
    OrganizationListView,
    organization_create_view
)

urlpatterns = [
    path('organization/', OrganizationListView.as_view(), name='organization-list'),
    path('organization/<int:pk>/', OrganizationDetailView.as_view(), name='organization-detail'),
    path('organization/new', organization_create_view, name='organization-create' ),
    path('organization/<int:pk>/update/', OrganizationUpdateView.as_view(), name='organization-update'),
    path('organization/<int:pk>/delete/', OrganizationDeleteView.as_view(), name='organization-delete'),
    ]