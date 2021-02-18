from django.urls import path
from . import views
from .views import (
    LabelCreateView,
    LabelDetailView,
    LabelDeleteView,
    LabelUpdateView,
    LabelListView
)
urlpatterns = [
    path('label/', LabelListView.as_view(), name='label-list'),
    path('label/<int:pk>/', LabelDetailView.as_view(), name='label-detail'),
    path('label/new/', LabelCreateView.as_view(), name='label-create'),
    path('label/<int:pk>/update/', LabelUpdateView.as_view(), name='label-update'),
    path('label/<int:pk>/delete/', LabelDeleteView.as_view(), name='label-delete'),
    ]