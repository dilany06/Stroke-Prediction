from django.shortcuts import render,redirect
from .forms import StrokeForm
import pandas as pd
import joblib

from sklearn.preprocessing import LabelEncoder
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User

model = joblib.load('my_stroke_model.pkl')
label_encoders = joblib.load('my_label_encoders.pkl')

# Create your views here.
def home(request):
    return render(request,'index.html',{})

def upload(request):
    result = None  # Initially no result
    if request.method == 'POST':  # If the form is submitted (POST request)
        form = StrokeForm(request.POST)  # Create a form object with the submitted data
        if form.is_valid():  # If the form is valid
            data = form.cleaned_data  # Cleaned data (formatted data from the form)
            df = pd.DataFrame([data])  # Convert the cleaned data into a DataFrame

            # Drop the 'id' column if it exists in the DataFrame
            if 'id' in df.columns:
                df = df.drop(columns=['id'])

            # Define which columns need to be encoded (categorical columns)
            categorical_columns = ['gender', 'hypertension', 'heart_disease', 'ever_married',
                                   'work_type', 'Residence_type', 'smoking_status']
            
            # Encode the categorical features using the loaded label encoders
            for col in categorical_columns:
                if col in df.columns and col in label_encoders:  # Check if the column exists in both DataFrame and encoders
                    df[col] = label_encoders[col].transform(df[col])  # Apply the encoding

            # Make a prediction using the model
            prediction = model.predict(df)[0]  # Predict using the model (returns a single value)
            
            # Show the result based on the prediction
            result = "Stroke Risk Detected" if prediction == 1 else "No Stroke Risk"
    else:
        form = StrokeForm()  # If no data is submitted, just display an empty form

    # Render the template with the form and the result
    return render(request, 'upload.html', {'form': form, 'result': result})

def analysis(request):
    return render(request,'analysis.html',{})

def causes(request):
    return render(request,'causes.html',{})

from .models import Appointment
from .forms import AppointmentForm

def appointment_booking(request):

    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')  # Redirect to a success page after booking
    else:
        form = AppointmentForm()

    return render(request, 'booking.html', {'form': form})

def appointment_success(request):
    return render(request, 'success.html')

def appointment_list(request):
    appointments = Appointment.objects.all()  # Fetch all appointments
    return render(request, 'list.html', {'appointments': appointments})

   
def signup(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = User.objects.create_user(username=username,password=password,email=email)
        return redirect('login')
    return render(request,"signup.html",{})  

def app_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username=username,password=password) 
        if user is not None:
            login(request,user)

            return redirect('home')
    return render(request,"login.html",{})





