from django.forms import ModelForm, TextInput
from .models import Patient, MedicalHistory

class PatientForm(ModelForm):
    class Meta:
        model = Patient
        fields = '__all__'

class MedicalHistoryForm(ModelForm):
    
    class Meta:
        model = MedicalHistory
        fields = '__all__'
