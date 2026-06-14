import unittest


class Patient:
    def __init__(self, name, year_birth, is_healthy):
        self.name = name
        self.year_birth = year_birth
        self.is_healthy = is_healthy

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


class TestPatient(unittest.TestCase):

    def setUp(self):
        self.old_unhealthy = Patient('Иванов', 1940, False)
        self.adult_healthy = Patient('Петров', 1970, True)
        self.young_healthy = Patient('Сидоров', 1995, True)

    def test_health_status_define(self):
        self.assertEqual(self.old_unhealthy.health_status_define(), 'Болен')
        self.assertEqual(self.adult_healthy.health_status_define(), 'Здоров')
        self.assertEqual(self.young_healthy.health_status_define(), 'Здоров')

    def test_age_category_define(self):
        self.assertEqual(self.old_unhealthy.age_category_define(), 'Пожилой')
        self.assertEqual(self.adult_healthy.age_category_define(), 'Взрослый')
        self.assertEqual(self.young_healthy.age_category_define(), 'Молодой')


if __name__ == '__main__':
    unittest.main()