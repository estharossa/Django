from django.urls import path
from . import views

urlpatterns = [
    path('todos/', views.todo_list),
    path('todos/completed/', views.completed_todo_list)
]