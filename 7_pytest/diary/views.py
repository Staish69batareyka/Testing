from django.shortcuts import render, get_object_or_404
from .models import Patient

def patient_list(request):
    patients = Patient.objects.all()
    context = {'patient_list': patients}
    return render(request, 'diary/patient_list.html', context)

def patient_detail(request, pk):
    patient = get_object_or_404(Patient, pk=pk)
    context = {'patient': patient}
    return render(request, 'diary/patient_detail.html', context)