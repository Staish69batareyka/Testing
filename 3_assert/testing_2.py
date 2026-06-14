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


test_old_unhealthy = Patient('Иванов', 1940, False)
assert test_old_unhealthy.health_status_define() == 'Болен'
assert test_old_unhealthy.age_category_define() == 'Пожилой'

test_adult_healthy = Patient('Петров', 1970, True)
assert test_adult_healthy.health_status_define() == 'Здоров'
assert test_adult_healthy.age_category_define() == 'Взрослый'

test_young_healthy = Patient('Сидоров', 1995, True)
assert test_young_healthy.health_status_define() == 'Здоров'
assert test_young_healthy.age_category_define() == 'Молодой'