from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Doctor, Patient, Appointment
from .serializers import DoctorSerializer, PatientSerializer, AppointmentSerializer
from django.shortcuts import render
from .models import Doctor, Patient, Appointment


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

def dashboard(request):

    doctors = Doctor.objects.count()
    patients = Patient.objects.count()
    appointments = Appointment.objects.all()[:5]

    context = {
        'doctors': doctors,
        'patients': patients,
        'appointments_count': Appointment.objects.count(),
        'appointments': appointments
    }

    return render(request, 'dashboard.html', context)

def doctors(request):

    doctors = Doctor.objects.all()

    return render(request,'doctors.html',{'doctors':doctors})
def patients(request):

    patients = Patient.objects.all()

    return render(request,'patients.html',{'patients':patients})
def appointments(request):

    appointments = Appointment.objects.all()

    return render(request,'appointments.html',{'appointments':appointments})