from django.shortcuts import render, redirect
from django.http import HttpRequest
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .decorators import login_not_required
from .forms import AddPatientForm
from .models import Patient

# Create your views here.
@login_not_required
def index(request: HttpRequest):
  return render(request, 'pages/index.html')

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

@login_required(login_url='sign-in')
def dashboard(request: HttpRequest):
  return render(request, 'pages/dashboard-home.html')

@login_required(login_url='sign-in')
def addPatient(request: HttpRequest):
  form = AddPatientForm(request.POST)
  if request.method == 'POST':
    if form.is_valid():
      form.save()
      messages.success(request=request, message='Patient created successfully')
    else:
      print(form.errors)
  else:
    form = AddPatientForm()
  context = { 'form': form }
  return render(request, 'pages/add-patient.html', context=context)

@login_required(login_url='sign-in')
def patientList(request: HttpRequest):
  patients = Patient.objects.all()
  context = { 'patients': patients }
  return render(request, 'pages/patient-list.html', context=context)