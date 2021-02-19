from django.urls import path, include

from version_control.branches.views import BranchListView, BranchDetailView, BranchCreateView, BranchUpdateView, \
    BranchDeleteView

urlpatterns = [
    path('branches/', BranchListView.as_view(), name='branch-list'),
    path('branches/<int:pk>/', BranchDetailView.as_view(), name='branch-detail'),
    path('branch/new/', BranchCreateView.as_view(), name='branch-create'),
    path('branches/<int:pk>/update/', BranchUpdateView.as_view(), name='branch-update'),
    path('branches/<int:pk>/delete/', BranchDeleteView.as_view(), name='branch-delete'),
    path('branches/<int:branchId>/', include('version_control.commits.urls')),

]
