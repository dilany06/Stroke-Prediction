from django import forms

class StrokeForm(forms.Form):
    gender = forms.ChoiceField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')])
    age = forms.FloatField()
    hypertension = forms.ChoiceField(choices=[(0, 'No'), (1, 'Yes')])
    heart_disease = forms.ChoiceField(choices=[(0, 'No'), (1, 'Yes')])
    ever_married = forms.ChoiceField(choices=[('Yes', 'Yes'), ('No', 'No')])
    work_type = forms.ChoiceField(choices=[
         ('Private', 'Private'), ('Self-employed', 'Self-employed'),
        ('Govt_job', 'Govt Job'), ('children', 'Children'), ('Never_worked', 'Never Worked')
    ])
    Residence_type = forms.ChoiceField(choices=[('Urban', 'Urban'), ('Rural', 'Rural')])
    avg_glucose_level = forms.FloatField()
    bmi = forms.FloatField()
    smoking_status = forms.ChoiceField(choices=[
        ('formerly smoked', 'Formerly Smoked'), ('never smoked', 'Never Smoked'),
        ('smokes', 'Smokes'), ('Unknown', 'Unknown')
    ])

from django import forms
from .models import Appointment

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = [ 'patient_name', 'patient_email', 'patient_contact_number', 'appointment_date', 'appointment_time']
        
        widgets = {
            'appointment_date': forms.DateInput(attrs={'type': 'date'}),
            'appointment_time': forms.Select(choices=[('10:00 AM', '10:00 AM'), ('11:00 AM', '11:00 AM'), ('12:00 PM', '12:00 PM'), ('1:00 PM', '1:00 PM'), ('2:00 PM', '2:00 PM')]), 
        }
