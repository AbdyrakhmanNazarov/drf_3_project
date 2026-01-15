FROM python:3.11-alpine

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Зависимости для сборки Python пакетов
RUN apk add --no-cache build-base postgresql-dev libffi-dev jpeg-dev zlib-dev bash curl

# Копируем requirements и устанавливаем
COPY requirements.txt /app/
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

# Копируем весь проект
COPY . /app

# Запуск по умолчанию
CMD ["gunicorn", "myshop.wsgi:application", "--bind", "0.0.0.0:8003"]
