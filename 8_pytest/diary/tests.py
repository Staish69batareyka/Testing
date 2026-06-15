import pytest
from django.urls import reverse
from .models import Patient


@pytest.fixture
def old_unhealthy(db):
    return Patient.objects.create(name='Иванов', year_birth=1940, is_healthy=False)


@pytest.fixture
def adult_healthy(db):
    return Patient.objects.create(name='Петров', year_birth=1970, is_healthy=True)


@pytest.fixture
def young_healthy(db):
    return Patient.objects.create(name='Сидоров', year_birth=1995, is_healthy=True)


@pytest.fixture
def doctor_client(client, django_user_model):
    doctor = django_user_model.objects.create_user(username='doctor', password='password')
    client.login(username='doctor', password='password')
    return client


@pytest.fixture
def user_client(client, django_user_model):
    user = django_user_model.objects.create_user(username='user', password='password')
    client.login(username='user', password='password')
    return client


def test_health_status_define(old_unhealthy, adult_healthy, young_healthy):
    assert old_unhealthy.health_status_define() == 'Болен'
    assert adult_healthy.health_status_define() == 'Здоров'
    assert young_healthy.health_status_define() == 'Здоров'


def test_age_category_define(old_unhealthy, adult_healthy, young_healthy):
    assert old_unhealthy.age_category_define() == 'Пожилой'
    assert adult_healthy.age_category_define() == 'Взрослый'
    assert young_healthy.age_category_define() == 'Молодой'


def test_patient_list_view_authenticated(doctor_client, old_unhealthy, adult_healthy, young_healthy):
    response = doctor_client.get(reverse('patient_list'))
    assert response.status_code == 200
    assert 'diary/patient_list.html' in [t.name for t in response.templates]

    content = response.content.decode('utf-8')
    assert 'Иванов' in content
    assert 'Петров' in content
    assert 'Сидоров' in content


def test_patient_detail_view_authenticated(doctor_client, old_unhealthy):
    response = doctor_client.get(reverse('patient_detail', kwargs={'pk': old_unhealthy.pk}))
    assert response.status_code == 200
    assert 'diary/patient_detail.html' in [t.name for t in response.templates]

    content = response.content.decode('utf-8')
    assert 'Иванов' in content


def test_anonymous_user_cannot_access_patient_list(client):
    response = client.get(reverse('patient_list'))
    assert response.status_code in [302, 403]


def test_anonymous_user_cannot_access_patient_detail(client, old_unhealthy):
    response = client.get(reverse('patient_detail', kwargs={'pk': old_unhealthy.pk}))
    assert response.status_code in [302, 403]