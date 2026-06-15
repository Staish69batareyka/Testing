from django.test import TestCase
from django.urls import reverse
from .models import Patient


class PatientTestCase(TestCase):

    def setUp(self):
        self.old_unhealthy = Patient.objects.create(
            name='Иванов',
            year_birth=1940,
            is_healthy=False
        )
        self.adult_healthy = Patient.objects.create(
            name='Петров',
            year_birth=1970,
            is_healthy=True
        )
        self.young_healthy = Patient.objects.create(
            name='Сидоров',
            year_birth=1995,
            is_healthy=True
        )

    def test_health_status_define(self):
        self.assertEqual(self.old_unhealthy.health_status_define(), 'Болен')
        self.assertEqual(self.adult_healthy.health_status_define(), 'Здоров')
        self.assertEqual(self.young_healthy.health_status_define(), 'Здоров')

    def test_age_category_define(self):
        self.assertEqual(self.old_unhealthy.age_category_define(), 'Пожилой')
        self.assertEqual(self.adult_healthy.age_category_define(), 'Взрослый')
        self.assertEqual(self.young_healthy.age_category_define(), 'Молодой')

    def test_patient_list_view(self):
        response = self.client.get(reverse('patient_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'diary/patient_list.html')
        self.assertContains(response, 'Иванов')
        self.assertContains(response, 'Петров')
        self.assertContains(response, 'Сидоров')

    def test_patient_detail_view(self):
        response = self.client.get(
            reverse('patient_detail', kwargs={'pk': self.old_unhealthy.pk})
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'diary/patient_detail.html')
        self.assertContains(response, 'Иванов')