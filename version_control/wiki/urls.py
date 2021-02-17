from django.urls import path
from .views import (
    WikiCreateView,
)

urlpatterns = [
    path('wiki', WikiCreateView.as_view(), name='wiki-create'),
]
