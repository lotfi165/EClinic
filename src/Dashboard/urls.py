from django.urls import path
from . import views

urlpatterns = [
  path('', views.index, name='index'),
  path('sign-in/', views.signIn, name='sign-in'),
  path('sign-out/', views.signOut, name='sign-out'),
  path('dashboard/', views.dashboard, name='dashboard'),
  path('dashboard/patients', views.patientList, name='patient-list'),
  path('dashboard/patients/add', views.addPatient, name='add-patient'),
  path('dashboard/patients/edit/<str:patientId>/', views.editPatient, name='edit-patient'),
  path('dashboard/patients/edit/<str:patientId>/history', views.editMedicalHistory, name='edit-medical-history'),
  path('dashboard/patients/delete/<str:patientId>/', views.deletePatient, name='delete-patient'),
]
