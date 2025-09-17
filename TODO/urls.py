from django.urls import path,include
from .views import CreateTodo,ViewTodo
urlpatterns = [
    path('view-todo',ViewTodo.as_view(),name="view TODO"),
    path('create-todo',CreateTodo.as_view(),name="create TODO"),
]
