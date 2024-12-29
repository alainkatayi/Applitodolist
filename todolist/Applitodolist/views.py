from django.contrib. auth.decorators import login_required
from django.shortcuts import render, redirect,get_object_or_404
from django.http import HttpResponse
from django.template import loader
from .models import Task
#from .forms import ConnexionForm
#from .models import  User
from .forms import SimpleForm, TaskForm

# Create your views here.
@login_required
def index(request):
    #template = loader.get_template("Applitodolist/index.html")

    #context ={"form" : "yes"}
    
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
    


"""def login(request):
    return render(request, 'Applitodolist/login.html')"""

"""def submit_form(request):
    
    if request.method == 'POST':
        form = ConnexionForm (request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('soumission reussis')
        
    return render ('Applitodolist/login.html', {'form': form})"""


    

"""def sign_up(request):
    form = SimpleForm()
    return render (request, 'Applitodolist/sign_up.html', {'form': form})
    return render (request, 'Applitodolist/sign_up.html')"""



"""def show_form (request):
    form = SimpleForm()
    if request.method == 'POST':
        form = SimpleForm(request.POST)
        if form.is_valid ():
            name = form.cleaned_data ['name']
            password = form.cleaned_data ['password']

            return render (request, 'Applitodolist/login.html', {'name': name})
    else:
        form = SimpleForm ()
    return render (request, 'Applitodolist/sign_up.html', {'form': form})"""


"""def chow_form (request):

        return"""



"""def sign_up(request):
    if  request.method == 'POST':
        form = SimpleForm(request.POST)

        if form.is_valid():
            return render (request, 'Applitodolist/success.html')
    else:
        form = SimpleForm()
    context = {"form": form}
    return render (request, 'Applitodolist/sign_up.html', context )"""

"""def succ(request):
    return render (request, 'Applitodolist/success.html')"""
    
