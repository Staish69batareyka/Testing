from django.db import models
from django.contrib.auth import get_user_model

class Patient(models.Model):
    name = models.CharField(max_length=100)
    year_birth = models.IntegerField()
    is_healthy = models.BooleanField(default=True)

    def age_category_define(self):
        if 1946 < self.year_birth < 1980:
            return 'Взрослый'
        if self.year_birth >= 1980:
            return 'Молодой'
        return 'Пожилой'

    def health_status_define(self):
        if self.is_healthy:
            return 'Здоров'
        return 'Болен'

    def show_patient(self):
        return (
            f'{self.name}, '
            f'возраст: {self.age_category_define()}, '
            f'статус: {self.health_status_define()}'
        )

User = get_user_model()

class MedicalRecord(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    slug = models.SlugField(unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title