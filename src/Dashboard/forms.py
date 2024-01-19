from django.forms import ModelForm, TextInput
from .models import Patient

class PatientForm(ModelForm):
    class Meta:
        model = Patient
        fields = '__all__'
