from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView
from .models import ToDoList, ToDoItem

class todo_list(ListView):
    model = ToDoList
    context_object_name = 'todolist'

def index(request):
    return render(request,'todo/index.html')

