from django.urls import path
from . import views

urlpatterns = [
    path('todo_list/', views.index, name='todo_list'),
    path('create/', views.addTodo, name='create'),
    path('update_status/<id>', views.changeTodoStatus, name='update_status'),
    path('delete/<id>', views.delelteById, name='delete')
]
