from django.urls import path
from .views import presentation, auth, patient, doctor, department, speciality, procedures, appointement

urlpatterns = [
  path('', presentation.index, name='index'),
  path('dashboard/', presentation.dashboard, name='dashboard'),

  path('sign-in/', auth.signIn, name='sign-in'),
  path('sign-out/', auth.signOut, name='sign-out'),

  path('dashboard/patients', patient.patientList, name='patient-list'),
  path('dashboard/patients/add', patient.addPatient, name='add-patient'),
  path('dashboard/patients/edit/<str:patientId>/', patient.editPatient, name='edit-patient'),
  path('dashboard/patients/edit/<str:patientId>/history', patient.editMedicalHistory, name='edit-medical-history'),
  path('dashboard/patients/delete/<str:patientId>/', patient.deletePatient, name='delete-patient'),

  path('dashboard/doctors', doctor.doctorList, name='doctor-list'),
  path('dashboard/doctors/add', doctor.addDoctor, name='add-doctor'),
  path('dashboard/doctors/edit/<str:doctorId>/', doctor.editDoctor, name='edit-doctor'),
  path('dashboard/doctors/delete/<str:doctorId>/', doctor.deleteDoctor, name='delete-doctor'),

  path('dashboard/departments', department.departmentList, name='department-list'),
  path('dashboard/departments/add', department.addDepartment, name='add-department'),
  path('dashboard/departments/edit/<str:departmentId>/', department.editDepartment, name='edit-department'),
  path('dashboard/departments/delete/<str:departmentId>/', department.deleteDepartment, name='delete-department'),

  path('dashboard/specialities', speciality.specialityList, name='speciality-list'),
  path('dashboard/specialities/add', speciality.addSpeciality, name='add-speciality'),
  path('dashboard/specialities/edit/<str:specialityId>/', speciality.editSpeciality, name='edit-speciality'),
  path('dashboard/specialities/delete/<str:specialityId>/', speciality.deleteSpeciality, name='delete-speciality'),

  path('dashboard/procedures', procedures.procedureList, name='procedure-list'),
  path('dashboard/procedures/add', procedures.addProcedure, name='add-procedure'),
  path('dashboard/procedures/edit/<str:procedureId>/', procedures.editProcedure, name='edit-procedure'),
  path('dashboard/procedures/delete/<str:procedureId>/', procedures.deleteProcedure, name='delete-procedure'),

  path('dashboard/appointments/patient/<str:patientId>/add', appointement.addAppointement, name='add-appointment'),
  path('dashboard/appointments/edit/<str:patientId>', appointement.editAppointment, name='edit-appointment'),
]
