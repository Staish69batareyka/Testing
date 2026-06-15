import pytest
from .models import Patient


@pytest.fixture
def old_unhealthy():
    return Patient(name='Иванов', year_birth=1940, is_healthy=False)


@pytest.fixture
def adult_healthy():
    return Patient(name='Петров', year_birth=1970, is_healthy=True)


@pytest.fixture
def young_healthy():
    return Patient(name='Сидоров', year_birth=1995, is_healthy=True)


def test_health_status_define(old_unhealthy, adult_healthy, young_healthy):
    assert old_unhealthy.health_status_define() == 'Болен'
    assert adult_healthy.health_status_define() == 'Здоров'
    assert young_healthy.health_status_define() == 'Здоров'


def test_age_category_define(old_unhealthy, adult_healthy, young_healthy):
    assert old_unhealthy.age_category_define() == 'Пожилой'
    assert adult_healthy.age_category_define() == 'Взрослый'
    assert young_healthy.age_category_define() == 'Молодой'


def test_patient_list_view(client, db):
    Patient.objects.create(name='Иванов', year_birth=1940, is_healthy=False)
    Patient.objects.create(name='Петров', year_birth=1970, is_healthy=True)
    Patient.objects.create(name='Сидоров', year_birth=1995, is_healthy=True)

    response = client.get('/patients/')
    assert response.status_code == 200
    assert 'diary/patient_list.html' in [t.name for t in response.templates]

    content = response.content.decode('utf-8')
    assert 'Иванов' in content
    assert 'Петров' in content
    assert 'Сидоров' in content


def test_patient_detail_view(client, db):
    patient = Patient.objects.create(name='Иванов', year_birth=1940, is_healthy=False)

    response = client.get(f'/patients/{patient.pk}/')
    assert response.status_code == 200
    assert 'diary/patient_detail.html' in [t.name for t in response.templates]

    content = response.content.decode('utf-8')
    assert 'Иванов' in content