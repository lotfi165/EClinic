from django.shortcuts import render
from django.http import HttpRequest
from django.contrib.auth.decorators import login_required
from ..decorators import login_not_required
from ..models import Patient, MedicalStaff, Department, Speciality, Appointment, Procedure, ProcedureApplication

# Create your views here.
@login_not_required
def index(request: HttpRequest):
  return render(request, 'pages/presentation/index.html')

@login_required(login_url='sign-in')
def dashboard(request: HttpRequest):
  patientCount = Patient.objects.count()
  medicalStaffCount = MedicalStaff.objects.count()
  departmentCount = Department.objects.count()
  specialityCount = Speciality.objects.count()
  appointmentCount = Appointment.objects.count()

  departments = Department.objects.all()
  departmentMedicalStaffCount = {}
  for department in departments:
    medicalStaffCount = MedicalStaff.objects.filter(department=department.id).count()
    departmentMedicalStaffCount[department.name] = medicalStaffCount
  departmentMedicalStaffCountKeys = list(departmentMedicalStaffCount.keys())
  departmentMedicalStaffCountValues = list(departmentMedicalStaffCount.values())

  specialities = Speciality.objects.all()
  specialityMedicalStaffCount = {}
  for speciality in specialities:
    medicalStaffCount = MedicalStaff.objects.filter(speciality=speciality).count()
    specialityMedicalStaffCount[speciality.name] = medicalStaffCount
  specialityMedicalStaffCountKeys = list(specialityMedicalStaffCount.keys())
  specialityMedicalStaffCountValues = list(specialityMedicalStaffCount.values())

  procedures = Procedure.objects.all()
  procedureApplicationCount = {}
  for procedure in procedures:
    procedureApplicationCountNumber = ProcedureApplication.objects.filter(procedure=procedure).count()
    procedureApplicationCount[procedure.name] = procedureApplicationCountNumber
  procedureApplicationCountKeys = list(procedureApplicationCount.keys())
  procedureApplicationCountValues = list(procedureApplicationCount.values())

  context = {
    'patientCount': patientCount,
    'medicalStaffCount': medicalStaffCount,
    'departmentCount': departmentCount,
    'specialityCount': specialityCount,
    'appointmentCount': appointmentCount,

    'departmentMedicalStaffCountKeys': departmentMedicalStaffCountKeys,
    'departmentMedicalStaffCountValues': departmentMedicalStaffCountValues,

    'specialityMedicalStaffCountKeys': specialityMedicalStaffCountKeys,
    'specialityMedicalStaffCountValues': specialityMedicalStaffCountValues,

    'procedureApplicationCountKeys': procedureApplicationCountKeys,
    'procedureApplicationCountValues': procedureApplicationCountValues
  }
  return render(request, 'pages/presentation/dashboard-home.html', context=context)