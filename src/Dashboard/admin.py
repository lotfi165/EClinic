from django.contrib import admin
from .models import Patient, MedicalHistory, Doctor, Department, Speciality, Procedure, Appointment, Prescription

# Register your models here.
admin.site.register(Patient)
admin.site.register(MedicalHistory)
admin.site.register(Doctor)
admin.site.register(Department)
admin.site.register(Speciality)
admin.site.register(Procedure)
admin.site.register(Appointment)
admin.site.register(Prescription)