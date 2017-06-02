from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm

from .forms import LoginForm

def index(request):
    return HttpResponse("Hello, world. You're at the home page.")


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user_login')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})


def user_login(request):
    if request.user.is_authenticated:
            return redirect('index')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponse("valid login")
        else:
            return HttpResponse("invalid login")
    else:
        form = LoginForm()
        return render(request, 'login.html', {'form':form})

def user_logout(request):
    if request.user.is_authenticated:
        logout(request)
        return HttpResponse("logged out")
    else:
        return redirect('index')
