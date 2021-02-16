from django.urls import path

from .views import (
    MilestoneCreateView,
    MilestoneDetailView,
    MilestoneDeleteView,
    MilestoneUpdateView,
    MilestoneListView
)

urlpatterns = [
    path('milestones/', MilestoneListView.as_view(), name='milestone-list'),
    path('milestone/<int:pk>/', MilestoneDetailView.as_view(), name='milestone-detail'),
    path('milestone/new/', MilestoneCreateView.as_view(), name='milestone-create'),
    path('milestone/<int:pk>/update/', MilestoneUpdateView.as_view(), name='milestone-update'),
    path('milestone/<int:pk>/delete/', MilestoneDeleteView.as_view(), name='milestone-delete'),
]
