from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Patient

def patient_list(request):
    patients = Patient.objects.all()
    output = ", ".join([p.name for p in patients])
    return HttpResponse(output)

def patient_detail(request, pk):
    patient = get_object_or_404(Patient, pk=pk)
    return HttpResponse(patient.name)