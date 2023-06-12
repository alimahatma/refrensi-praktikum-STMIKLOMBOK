from django.urls import path
from . import views
from . views import todo_list, index


urlpatterns = [
    path("", views.index, name="index"),
    path("todolist/", todo_list.as_view(template_name="todo/list.html"), name="todolist")
]