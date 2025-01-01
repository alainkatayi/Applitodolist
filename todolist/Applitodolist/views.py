from django.contrib. auth.decorators import login_required
from django.shortcuts import render, redirect,get_object_or_404
from django.template import loader
from .models import Task
from .forms import TaskForm

# Create your views here.
@login_required
def index(request):
    context = {"task": Task.objects.filter(user=request.user)}
    return render (request, 'Applitodolist/index.html', context)


def show (request, task_id):
    context = {"tasks": get_object_or_404(Task, pk = task_id) }
    return render (request, 'Applitodolist/show.html', context)


def create_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit = False)
            task.user = request.user
            task.save()
            return redirect ('Applitodolist:index')
    else:
        form = TaskForm()
    return render(request, 'Applitodolist/task.html', {"form": form})