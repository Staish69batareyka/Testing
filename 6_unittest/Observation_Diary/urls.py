from django.contrib import admin
from django.urls import path
from diary import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('patients/', views.patient_list, name='patient_list'),
    path('patients/<int:pk>/', views.patient_detail, name='patient_detail'),
]