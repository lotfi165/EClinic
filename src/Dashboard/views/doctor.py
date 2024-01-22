from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpRequest
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from ..forms import SearchForm, DoctorForm
from ..models import Doctor
from django.db.models import Q

# Create your views here.
@login_required(login_url='sign-in')
def addDoctor(request: HttpRequest):
  form = DoctorForm(request.POST)
  if request.method == 'POST':
    if form.is_valid():
      form.save()
      messages.success(request=request, message='Doctor created successfully')
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