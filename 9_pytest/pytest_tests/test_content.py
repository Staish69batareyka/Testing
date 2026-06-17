# test_content.py
from django.urls import reverse


def test_medical_record_in_list_for_author(record, author_client):
    url = reverse('records:list')
    response = author_client.get(url)
    object_list = response.context['object_list']
    assert record in object_list


def test_medical_record_not_in_list_for_another_user(record, not_author_client):
    url = reverse('records:list')
    response = not_author_client.get(url)
    object_list = response.context['object_list']
    assert record not in object_list


def test_create_and_edit_pages_contain_form(author_client, medical_record):
    urls = (
        reverse('records:create'),
        reverse('records:edit', args=(medical_record.slug,)),
    )
    for url in urls:
        response = author_client.get(url)
        assert 'form' in response.context