from django.urls import path

from version_control.branches.views import BranchListView, BranchDetailView, BranchCreateView, BranchUpdateView, \
    BranchDeleteView

urlpatterns = [
    path('branches/', BranchListView.as_view(), name='branch-list'),
    path('<slug:pk>/', BranchDetailView.as_view(), name='branch-detail'),
    path('branch/new/', BranchCreateView.as_view(), name='branch-create'),
    path('<slug:pk>/update/', BranchUpdateView.as_view(), name='branch-update'),
    path('<slug:pk>/delete/', BranchDeleteView.as_view(), name='branch-delete'),
]
