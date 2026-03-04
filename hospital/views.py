from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Doctor, Patient, Appointment
from .serializers import DoctorSerializer, PatientSerializer, AppointmentSerializer
from django.shortcuts import render
from .models import Doctor, Patient, Appointment
from django.core.paginator import Paginator
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

class DoctorViewSet(viewsets.ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    permission_classes = [IsAuthenticated]


class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    permission_classes = [IsAuthenticated]


class AppointmentViewSet(viewsets.ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
    permission_classes = [IsAuthenticated] 

@login_required
def dashboard(request):

    doctors = Doctor.objects.count()
    patients = Patient.objects.count()
    appointments_count = Appointment.objects.count()
    recent_appointments = Appointment.objects.all()[:5]

    context = {
        'doctors': doctors,
        'patients': patients,
        'appointments_count': appointments_count,
        'recent_appointments': recent_appointments
    }

    return render(request, 'dashboard.html', context)

@login_required
def doctors(request):

    query = request.GET.get('q')

    if query:
        doctor_list = Doctor.objects.filter(name__icontains=query)
    else:
        doctor_list = Doctor.objects.all()

    paginator = Paginator(doctor_list, 5)   
    page_number = request.GET.get('page')
    doctors = paginator.get_page(page_number)

    return render(request, 'doctors.html', {'doctors': doctors})

@login_required
def patients(request):

    query = request.GET.get('q')

    if query:
        patient_list = Patient.objects.filter(name__icontains=query)
    else:
        patient_list = Patient.objects.all()

    paginator = Paginator(patient_list, 5)   
    page_number = request.GET.get('page')
    patients = paginator.get_page(page_number)

    return render(request, 'patients.html', {'patients': patients})

@login_required
def appointments(request):

    appointments = Appointment.objects.all()

    return render(request, 'appointments.html', {'appointments': appointments})

from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect


def login_view(request):

    if request.method == "POST":

        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/dashboard/')

    return render(request,'login.html')
def logout_view(request):

    logout(request)

    return redirect('/')
def book_appointment(request):

    doctors = Doctor.objects.all()

    if request.method == "POST":

        patient_name = request.POST.get('patient_name')
        doctor_id = request.POST.get('doctor')
        date = request.POST.get('date')

        doctor = Doctor.objects.get(id=doctor_id)

        patient, created = Patient.objects.get_or_create(name=patient_name)

        Appointment.objects.create(
            patient=patient,
            doctor=doctor,
            appointment_date=date,
            status="Pending"
        )

    return render(request,'book_appointment.html',{'doctors':doctors})