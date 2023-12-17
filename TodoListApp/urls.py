from django.urls import path
from .views import TodoListCreateView, TodoDetailView


urlpatterns = [
    path('todolist/', TodoListCreateView.as_view(), name='todo-list-create'),
    path('todolist/<int:pk>/', TodoDetailView.as_view(), name='todo-details')
]