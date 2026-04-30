from django.db import models

# Create your models here.
from django.db import models



class Appointment(models.Model):
    patient_name = models.CharField(max_length=100)
    patient_email = models.EmailField()
    patient_contact_number = models.CharField(max_length=15)
    appointment_date = models.DateField()
    appointment_time = models.CharField(max_length=50)  # Example: "10:00 AM"

    def __str__(self):
        return f"Appointment with {self.doctor.name} on {self.appointment_date} at {self.appointment_time}"
