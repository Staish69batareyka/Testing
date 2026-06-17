import pytest
from django.contrib.auth import get_user_model
from diary.models import MedicalRecord # Укажите правильный путь к моделям

User = get_user_model()

# Фикстура для обычного клиента (автора)
@pytest.fixture
def author(db):
    return User.objects.create_user(username='author', password='password123')

@pytest.fixture
def author_client(client, author):
    client.force_login(author)
    return client

# Фикстура для другого пользователя (не автора)
@pytest.fixture
def not_author(db):
    return User.objects.create_user(username='not_author', password='password123')

@pytest.fixture
def not_author_client(client, not_author):
    client.force_login(not_author)
    return client

# Фикстура медицинской записи (для тестов, запрашивающих 'record' и 'medical_record')
@pytest.fixture
def medical_record(db, author):
    return MedicalRecord.objects.create(
        title='Тестовая запись',
        description='Описание',
        slug='test-slug',
        author=author # Если у вас есть связь с автором в модели
    )

# Так как в ваших тестах контента используется имя 'record',
# а в тестах логики 'medical_record', можно сделать фикстуру-алиас:
@pytest.fixture
def record(medical_record):
    return medical_record

# Фикстура для аргументов (slug)
@pytest.fixture
def slug_for_args(medical_record):
    return (medical_record.slug,)

# Фикстура с данными формы для отправки POST-запросов
@pytest.fixture
def form_data():
    return {
        'title': 'Новый заголовок',
        'description': 'Новое описание',
        'slug': 'new-slug'
    }