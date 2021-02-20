from django.urls import path
from .views import (
     task_table,
     task_create_view,
     TaskListView,
     TaskDetailView,
     TaskDeleteView,
     task_update_view,
     TaskRevisionListView
)

urlpatterns = [
     path('task/<int:tk>/delete',  TaskDeleteView.as_view(), name='task-delete'),
     path('task/<int:tk>/update',  task_update_view, name='task-update'),
     path('task/<int:tk>/',TaskDetailView.as_view(), name='task-detail'),
     path('task/new', task_create_view, name='task-create' ),
     path('taskTable/', task_table, name='task-table'), 
     path('task/', TaskListView.as_view(), name='task-list'),  
     path('task/<int:tk>/history', TaskRevisionListView.as_view(), name='task-history'),  
]