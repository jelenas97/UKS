from django.urls import path

from .views import (
    MilestonesCreateView,
    MilestonesDetailView,
    MilestonesDeleteView,
    MilestonesUpdateView,
    MilestonesListView
)

urlpatterns = [
    path('label/', MilestonesListView.as_view(), name='milestone-list'),
    path('label/<int:pk>/', MilestonesDetailView.as_view(), name='milestone-detail'),
    path('label/new/', MilestonesCreateView.as_view(), name='milestone-create'),
    path('label/<int:pk>/update/', MilestonesUpdateView.as_view(), name='milestone-update'),
    path('label/<int:pk>/delete/', MilestonesDeleteView.as_view(), name='milestone-delete'),
]
