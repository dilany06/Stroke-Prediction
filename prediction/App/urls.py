from django.urls import path
from .views import *

urlpatterns =[
    path('home',home,name='home'),
    path('upload/',upload,name='upload'),
    path('analysis/',analysis,name='analysis'),
    path('causes/',causes,name='causes'),
    path('appointment/', appointment_booking, name='booking'),
    path('success/',appointment_success, name='success'),
    path('appointments/', appointment_list, name='list'),
    path('',app_login,name='login'),
    path('signup/',signup,name="signup"),

]