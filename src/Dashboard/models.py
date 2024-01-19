from django.db import models
import uuid

# Create your models here.
class Genders(models.TextChoices):
  MALE = 'MALE',
  FEMALE = 'FEMALE'

class ProcedureType(models.TextChoices):
  MEDICAL = 'MEDICAL',
  ADMINISTRATIVE = 'ADMINISTRATIVE'

class AppointmentState(models.TextChoices):
  SCHEDULED = 'SCHEDULED',
  COMPLETED = 'COMPLETED'
  CANCELED = 'CANCELED'

class Patient(models.Model):
  id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  firstName = models.CharField(max_length=256, null=False)
  lastName = models.CharField(max_length=256, null=False)
  dateOfBirth = models.DateField(null=False)
  adress = models.CharField(max_length=256, null=False)
  phoneNumber = models.CharField(max_length=20, null=False)
  email = models.CharField(max_length=254, null=False)
  gender = models.CharField(max_length=6, choices=Genders.choices)
  createdAt = models.DateTimeField(auto_now_add=True)
  updatedAt = models.DateTimeField(auto_now=True)

class MedicalHistory(models.Model):
  id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  patient = models.OneToOneField('Patient', on_delete=models.CASCADE)
  notes = models.TextField()
  allergies = models.TextField()
  surgeries = models.TextField()
  medications = models.TextField()
  updatedAt = models.DateTimeField(auto_now=True)

class Doctor(models.Model):
  id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  department = models.OneToOneField('Department', on_delete=models.CASCADE)
  speciality = models.OneToOneField('Speciality', on_delete=models.CASCADE)
  firstName = models.CharField(max_length=256, null=False)
  lastName = models.CharField(max_length=256, null=False)
  dateOfBirth = models.DateField(null=False)
  adress = models.CharField(max_length=256, null=False)
  phoneNumber = models.CharField(max_length=20, null=False)
  email = models.CharField(max_length=254, null=False)
  gender = models.CharField(max_length=6, choices=Genders.choices)
  createdAt = models.DateTimeField(auto_now_add=True)
  updatedAt = models.DateTimeField(auto_now=True)

class Department(models.Model):
  id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  name = models.CharField(max_length=256, null=False)

class Speciality(models.Model):
  id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  name = models.CharField(max_length=256, null=False)

class Procedure(models.Model):
  id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  name = models.CharField(max_length=256, null=False)
  type = models.CharField(max_length=15, choices=ProcedureType.choices)

class Appointment(models.Model):
  id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  doctors = models.ManyToManyField('Doctor')
  procedures = models.ManyToManyField('Procedure')
  timestamp = models.DateTimeField()
  state = models.CharField(max_length=10, choices=AppointmentState.choices)
  createdAt = models.DateTimeField(auto_now_add=True)
  updatedAt = models.DateTimeField(auto_now=True)

class Prescription(models.Model):
  id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  appointment = models.ForeignKey('Appointment', on_delete=models.CASCADE)
  content = models.TextField()
