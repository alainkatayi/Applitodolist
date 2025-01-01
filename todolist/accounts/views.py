from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.
def login_user(request):

    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]

        user  = authenticate(request, username=username, password= password)

        if user is not None:
            login(request, user)
            return redirect('Applitodolist:index')
        else:
            messages.info (request, "Incorrect password or username")

    form = AuthenticationForm()
    return render (request, 'accounts/login.html', {"form": form})


def register_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("Applitodolist:index")
    else:
        form = UserCreationForm()
    return render(request, 'accounts/register.html', {"form": form})


def logout_user(request):
    logout(request)
    return redirect("Applitodolist:index")

