from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpRequest
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from ..forms import AppointmentForm
from ..models import Patient, Appointment
from django.db.models import Q

@login_required(login_url='sign-in')
def addAppointement(request: HttpRequest, patientId: str):
  patient = get_object_or_404(Patient, id=patientId)
  form = AppointmentForm(request.POST, initial={'patient': patient})
  if request.method == 'POST':
    if form.is_valid():
      appointment = form.save()
      messages.success(request=request, message='Appointment created successfully')
      return redirect('edit-appointment', appointmentId=appointment.id)
  else:
    form = AppointmentForm(initial={'patient': patient})
  context = { 'form': form, 'patient': patient }
  return render(request, 'pages/appointment/add-appointment.html', context=context)

@login_required(login_url='sign-in')
def editAppointment(request: HttpRequest, appointmentId: str):
  appointment = get_object_or_404(Appointment, id=appointmentId)
  patient = get_object_or_404(Patient, id=appointment.patient.id)
  form = AppointmentForm(instance=appointment, initial={'patient': patient})
  if request.method == 'POST':
    data = request.POST.copy() 
    data.appendlist('patient', patient)
    print(data)
    form = AppointmentForm(data=data, instance=appointment)
    if form.is_valid():
      form.save()
      messages.success(request=request, message='Appointment history updated successfully')
  context = { 'form': form, 'patient': patient }
  return render(request, 'pages/appointment/edit-appointment.html', context=context)