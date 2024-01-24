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
  phoneNumber = models.CharField(max_length=20, null=False, unique=True)
  email = models.CharField(max_length=254, null=False, unique=True)
  gender = models.CharField(max_length=6, choices=Genders.choices)
  createdAt = models.DateTimeField(auto_now_add=True)
  updatedAt = models.DateTimeField(auto_now=True)

  def __str__(self):
     return f"{self.lastName} {self.firstName}"

class MedicalHistory(models.Model):
  id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  patient = models.OneToOneField('Patient', on_delete=models.CASCADE)
  notes = models.TextField(null=True, blank=True)
  allergies = models.TextField(null=True, blank=True)
  surgeries = models.TextField(null=True, blank=True)
  medications = models.TextField(null=True, blank=True)
  updatedAt = models.DateTimeField(auto_now=True, blank=True)

class Doctor(models.Model):
  id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  department = models.ForeignKey('Department', on_delete=models.CASCADE)
  speciality = models.ForeignKey('Speciality', on_delete=models.CASCADE)
  firstName = models.CharField(max_length=256, null=False)
  lastName = models.CharField(max_length=256, null=False)
  dateOfBirth = models.DateField(null=False)
  adress = models.CharField(max_length=256, null=False)
  phoneNumber = models.CharField(max_length=20, null=False, unique=True)
  email = models.CharField(max_length=254, null=False, unique=True)
  gender = models.CharField(max_length=6, choices=Genders.choices)
  createdAt = models.DateTimeField(auto_now_add=True)
  updatedAt = models.DateTimeField(auto_now=True)

  def __str__(self):
     return f"{self.lastName} {self.firstName}"

class Department(models.Model):
  id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  name = models.CharField(max_length=256, null=False, unique=True)

  def __str__(self):
     return f"{self.name}"

class Speciality(models.Model):
  id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  name = models.CharField(max_length=256, null=False, unique=True)

  def __str__(self):
     return f"{self.name}"

class Procedure(models.Model):
  id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  name = models.CharField(max_length=256, null=False, unique=True)
  type = models.CharField(max_length=15, choices=ProcedureType.choices)

  def __str__(self):
     return f"{self.name}"
  
class ProcedureApplication(models.Model):
  appointment = models.ForeignKey('Appointment', on_delete=models.CASCADE)
  doctor = models.ForeignKey('Doctor', on_delete=models.CASCADE)
  procedure = models.ForeignKey('Procedure', on_delete=models.CASCADE)
  report = models.TextField()

class Appointment(models.Model):
  id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  patient = models.ForeignKey('Patient', on_delete=models.CASCADE)
  timestamp = models.DateTimeField()
  state = models.CharField(max_length=10, choices=AppointmentState.choices, default=AppointmentState.SCHEDULED, blank=True)
  createdAt = models.DateTimeField(auto_now_add=True)
  updatedAt = models.DateTimeField(auto_now=True)

class Prescription(models.Model):
  id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  appointment = models.ForeignKey('Appointment', on_delete=models.CASCADE)
  content = models.TextField()
