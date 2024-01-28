from Dashboard.models import Department, Appointment, AppointmentState, Genders, MedicalHistory, MedicalStaff, Patient, Prescription, Procedure, ProcedureApplication, ProcedureType, Speciality
import django

django.setup()

Department.objects.create(name='Cardiology')