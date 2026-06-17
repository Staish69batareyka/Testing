from django.urls import path
from . import views

app_name = 'records'

urlpatterns = [


    path('patients/', views.patient_list, name='patient_list'),
    path('patients/<int:pk>/', views.patient_detail, name='patient_detail'),
]