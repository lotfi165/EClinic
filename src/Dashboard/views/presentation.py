from django.shortcuts import render
from django.http import HttpRequest
from django.contrib.auth.decorators import login_required
from ..decorators import login_not_required

# Create your views here.
@login_not_required
def index(request: HttpRequest):
  return render(request, 'pages/presentation/index.html')

@login_required(login_url='sign-in')
def dashboard(request: HttpRequest):
  return render(request, 'pages/presentation/dashboard-home.html')