# Используйте базовый образ Python
FROM python:3.12

# Установка переменной окружения для запуска внутри контейнера
ENV PYTHONUNBUFFERED 1

# Создание директории приложения в контейнере
WORKDIR /app

# Установка зависимостей
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копирование кода приложения в контейнер
COPY . .

# Запуск FastAPI приложения
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "6000"]