from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

all_todos = [
    {
        'title': 'Do Homework',
        'created_at': '04/03/2020',
        'due_on': '06/03/2020',
        'owner': 'admin',
        'is_completed': False
    },
    {
        'title': 'Clean the house',
        'created_at': '04/03/2020',
        'due_on': '06/03/2020',
        'owner': 'admin',
        'is_completed': False
    },
    {
        'title': 'Buy products',
        'created_at': '04/03/2020',
        'due_on': '06/03/2020',
        'owner': 'admin',
        'is_completed': True
    },
    {
        'title': 'Go to the gym',
        'created_at': '04/03/2020',
        'due_on': '06/03/2020',
        'owner': 'admin',
        'is_completed': False
    },
    {
        'title': 'Go to the gym',
        'created_at': '04/03/2020',
        'due_on': '06/03/2020',
        'owner': 'admin',
        'is_completed': True
    }
]


def todo_list(request):
    context = {
        'todos': all_todos
    }
    return render(request, 'list.html', context=context)


def completed_todo_list(request):
    completed_todos = list(filter(lambda todo: (todo['is_completed'] == True), all_todos))
    context = {
        'todos': completed_todos
    }
    return render(request, 'list.html', context=context)
