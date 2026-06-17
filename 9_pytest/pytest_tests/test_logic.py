# test_logic.py
from http import HTTPStatus
from django.urls import reverse
from pytest_django.asserts import assertRedirects
from diary.models import MedicalRecord


def test_user_can_create_medical_record(author_client, form_data):
    url = reverse('records:create')
    response = author_client.post(url, data=form_data)
    assertRedirects(response, reverse('records:success'))
    assert MedicalRecord.objects.count() == 1
    new_record = MedicalRecord.objects.get()
    assert new_record.title == form_data['title']
    assert new_record.description == form_data['description']
    assert new_record.slug == form_data['slug']


def test_anonymous_user_cant_create_medical_record(client, form_data):
    url = reverse('records:create')
    response = client.post(url, data=form_data)
    expected_url = f"{reverse('users:login')}?next={url}"
    assertRedirects(response, expected_url)
    assert MedicalRecord.objects.count() == 0


def test_author_can_edit_medical_record(author_client, form_data, medical_record):
    url = reverse('records:edit', args=(medical_record.slug,))
    response = author_client.post(url, form_data)
    assertRedirects(response, reverse('records:success'))
    medical_record.refresh_from_db()
    assert medical_record.title == form_data['title']
    assert medical_record.description == form_data['description']
    assert medical_record.slug == form_data['slug']


def test_other_user_cant_edit_medical_record(not_author_client, form_data, medical_record):
    url = reverse('records:edit', args=(medical_record.slug,))
    response = not_author_client.post(url, form_data)
    assert response.status_code == HTTPStatus.NOT_FOUND
    record_from_db = MedicalRecord.objects.get(id=medical_record.id)
    assert medical_record.title == record_from_db.title
    assert medical_record.description == record_from_db.description
    assert medical_record.slug == record_from_db.slug


def test_author_can_delete_medical_record(author_client, slug_for_args):
    url = reverse('records:delete', args=slug_for_args)
    response = author_client.post(url)
    assertRedirects(response, reverse('records:success'))
    assert MedicalRecord.objects.count() == 0


def test_other_user_cant_delete_medical_record(not_author_client, slug_for_args):
    url = reverse('records:delete', args=slug_for_args)
    response = not_author_client.post(url)
    assert response.status_code == HTTPStatus.NOT_FOUND
    assert MedicalRecord.objects.count() == 1