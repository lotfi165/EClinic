from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpRequest
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from ..forms import AppointmentForm, SearchForm, ProcedureApplicationForm, AssignDoctorForm
from ..models import Patient, Appointment, Doctor, ProcedureApplication
from django.db.models import Q

@login_required(login_url='sign-in')
def applyProcedure(request: HttpRequest, appointmentId: str):
  appointment = get_object_or_404(Appointment, id=appointmentId)
  patient = get_object_or_404(Patient, id=appointment.patient.id)
  form = ProcedureApplicationForm(initial={'appointment': appointment})
  searchForm = SearchForm(request.GET)
  assignDoctorForm = AssignDoctorForm(request.POST)
  doctor = None
  doctors = []

  if request.method == 'POST':
    if request.POST.get('confirm'):
      data = request.POST.copy() 
      data.appendlist('appointment', appointment)
      form = ProcedureApplicationForm(data=data)
      if form.is_valid():
        form.save()
        messages.success(request=request, message='Procedure applied successfully')
        return redirect('edit-appointment', appointmentId=appointment.id)
    else:
      if assignDoctorForm.is_valid():
        if assignDoctorForm.cleaned_data['remove']:
          doctor = None
        else:
          doctor = get_object_or_404(Doctor, id=assignDoctorForm.cleaned_data['doctorId'])
  
  if searchForm.is_valid():
    search = searchForm.cleaned_data['search']
    if search:
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

  context = { 'form': form, 'searchForm': searchForm, 'assignDoctorForm': AssignDoctorForm(), 'removeDoctorForm': AssignDoctorForm(), 'patient': patient, 'appointment': appointment, 'doctor': doctor, 'doctors': doctors }
  return render(request, 'pages/appointment/apply-procedure.html', context=context)

@login_required(login_url='sign-in')
def deleteProcedureApplication(request: HttpRequest, procedureApplicationId: str):
  procedureApplication = get_object_or_404(ProcedureApplication, id=procedureApplicationId)
  appointment = procedureApplication.appointment
  procedureApplication.delete()
  return redirect('edit-appointment', appointmentId=appointment.id)