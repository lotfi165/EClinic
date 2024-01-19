from django.shortcuts import render, redirect
from django.http import HttpRequest
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .decorators import login_not_required

# Create your views here.
@login_not_required
def index(request: HttpRequest):
  return render(request, 'pages/index.html')

@login_required(login_url='sign-in')
def dashboard(request: HttpRequest):
  return render(request, 'pages/dashboard-home.html')

@login_not_required
def signIn(request: HttpRequest):
  if request.method == 'POST':
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request=request, username=username, password=password);
    if user is not None:
      login(request=request, user=user)
      return redirect('dashboard');
    else:
      messages.error(request=request, message="Wrong username or password");

  return render(request, 'pages/sign-in.html')

@login_required(login_url='sign-in')
def signOut(request: HttpRequest):
  logout(request=request)
  return redirect('sign-in');