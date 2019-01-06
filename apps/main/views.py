from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from django.http import Http404

from .models import Todo
from .forms import TodoForm

# Create your views here.
@login_required(login_url='/accounts/login/')
def index(request):
    todo_list = Todo.objects.filter(user=request.user)

    form = TodoForm()

    context = {
        'todo_list' : todo_list,
        'form' : form
    }
    return render(request, 'todo_list.html', context)

@require_POST
def addTodo(request):
    if not request.user.is_authenticated:
        raise Http404

    form = TodoForm(request.POST)

    if form.is_valid():
        todo = Todo()
        todo.description = request.POST['description']
        todo.user = request.user
        todo.save()

    return redirect('todo_list')

def changeTodoStatus(request, id):
    todo = Todo.objects.get(pk=id)
    todo.status = True
    todo.save()

    return redirect('todo_list')

def delelteById(request, id):
    todo = Todo.objects.get(id=int(id))
    todo.delete()

    return redirect('todo_list')