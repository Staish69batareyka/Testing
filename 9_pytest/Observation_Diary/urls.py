from django.contrib import admin
from django.urls import path, include  # Не забудьте импортировать include
from diary import views

# Задаем глобальное имя приложения для этого файла
app_name = 'records'

urlpatterns = [
    # 1. Если внутри diary.urls лежат те же самые маршруты,
    # меняем их namespace на 'records':
    path('', include('diary.urls', namespace='records')),

    path('admin/', admin.site.urls),

]