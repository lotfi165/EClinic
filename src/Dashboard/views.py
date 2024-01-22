from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpRequest
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .decorators import login_not_required
from .forms import PatientForm, MedicalHistoryForm, SignInForm, SearchForm, DoctorForm
from .models import Patient, MedicalHistory, Doctor
from django.db.models import Q

# Create your views here.
@login_not_required
def index(request: HttpRequest):
  return render(request, 'pages/index.html')

@login_not_required
def signIn(request: HttpRequest):
  form = SignInForm()
  if request.method == 'POST':
    form = SignInForm(request.POST)
    if form.is_valid():
      user = authenticate(request=request, username=form.cleaned_data['username'], password=form.cleaned_data['password'])
      if user is not None:
        login(request=request, user=user)
        return redirect('dashboard')
      else:
        messages.error(request=request, message="Wrong username or password")

  context = { 'form': form }
  return render(request, 'pages/sign-in.html', context=context)

@login_required(login_url='sign-in')
def signOut(request: HttpRequest):
  logout(request=request)
  return redirect('sign-in')

@login_required(login_url='sign-in')
def dashboard(request: HttpRequest):
  return render(request, 'pages/dashboard-home.html')

@login_required(login_url='sign-in')
def addPatient(request: HttpRequest):
  form = PatientForm(request.POST)
  if request.method == 'POST':
    if form.is_valid():
      patient = form.save()
      MedicalHistory.objects.create(patient=patient)
      messages.success(request=request, message='Patient created successfully')
    else:
      print(form.errors)
  else:
    form = PatientForm()
  context = { 'form': form }
  return render(request, 'pages/patient/add-patient.html', context=context)

@login_required(login_url='sign-in')
def editPatient(request: HttpRequest, patientId: str):
  patient = get_object_or_404(Patient, id=patientId)
  form = PatientForm(instance=patient)
  if request.method == 'POST':
    form = PatientForm(data=request.POST, instance=patient)
    if form.is_valid():
      form.save()
      messages.success(request=request, message='Patient updated successfully')
  context = { 'form': form }
  return render(request, 'pages/patient/edit-patient.html', context=context)

@login_required(login_url='sign-in')
def editMedicalHistory(request: HttpRequest, patientId: str):
  patient = get_object_or_404(Patient, id=patientId)
  medicalHistory = get_object_or_404(MedicalHistory, patient=patient)
  form = MedicalHistoryForm(instance=medicalHistory, initial={'patient': patient})
  if request.method == 'POST':
    data = request.POST.copy() 
    data.appendlist('patient', patient)
    print(data)
    form = MedicalHistoryForm(data=data, instance=medicalHistory)
    if form.is_valid():
      form.save()
      messages.success(request=request, message='Medical history updated successfully')
  context = { 'form': form, 'patient': patient }
  return render(request, 'pages/patient/edit-medical-history.html', context=context)

@login_required(login_url='sign-in')
def deletePatient(request: HttpRequest, patientId: str):
  patient = get_object_or_404(Patient, id=patientId)
  patient.delete()
  return redirect('patient-list')

@login_required(login_url='sign-in')
def patientList(request: HttpRequest):
  form = SearchForm(request.GET)
  patients = []
  if form.is_valid():
    search = form.cleaned_data['search']
    patients = Patient.objects.filter(
      Q(firstName__icontains=search) |
      Q(lastName__icontains=search) |
      Q(dateOfBirth__icontains=search) |
      Q(adress__icontains=search) |
      Q(phoneNumber__icontains=search) |
      Q(email__icontains=search) |
      Q(gender__icontains=search)
    )
  else:
    patients = Patient.objects.all()
  context = { 'patients': patients, 'form': form }
  return render(request, 'pages/patient/patient-list.html', context=context)

@login_required(login_url='sign-in')
def addDoctor(request: HttpRequest):
  form = DoctorForm(request.POST)
  if request.method == 'POST':
    if form.is_valid():
      form.save()
      messages.success(request=request, message='Doctor created successfully')
    else:
      print(form.errors)
  else:
    form = DoctorForm()
  context = { 'form': form }
  return render(request, 'pages/doctor/add-doctor.html', context=context)

@login_required(login_url='sign-in')
def editDoctor(request: HttpRequest, doctorId: str):
  doctor = get_object_or_404(Doctor, id=doctorId)
  form = DoctorForm(instance=doctor)
  if request.method == 'POST':
    form = DoctorForm(data=request.POST, instance=doctor)
    if form.is_valid():
      form.save()
      messages.success(request=request, message='Doctor updated successfully')
  context = { 'form': form }
  return render(request, 'pages/doctor/edit-doctor.html', context=context)

@login_required(login_url='sign-in')
def deleteDoctor(request: HttpRequest, doctorId: str):
  doctor = get_object_or_404(Doctor, id=doctorId)
  doctor.delete()
  return redirect('doctor-list')

@login_required(login_url='sign-in')
def doctorList(request: HttpRequest):
  form = SearchForm(request.GET)
  doctors = []
  if form.is_valid():
    search = form.cleaned_data['search']
    doctors = Doctor.objects.filter(
      Q(firstName__icontains=search) |
      Q(lastName__icontains=search) |
      Q(dateOfBirth__icontains=search) |
      Q(adress__icontains=search) |
      Q(phoneNumber__icontains=search) |
      Q(email__icontains=search) |
      Q(gender__icontains=search)
    )
  else:
    doctors = Doctor.objects.all()
  context = { 'doctors': doctors, 'form': form }
  return render(request, 'pages/doctor/doctor-list.html', context=context)