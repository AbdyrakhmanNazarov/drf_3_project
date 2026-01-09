# drf_3_project

REST API проект на Django Rest Framework с PostgreSQL CELERY REDIS и Docker.

## ⚠️ Порт
Порт **8000 8001 8002 заняты**, проект работает на **8003**

## 🚀 Запуск

```bash
docker compose build
docker compose up -d
docker compose exec web python manage.py migrate
docker compose exec web python manage.py createsuperuser