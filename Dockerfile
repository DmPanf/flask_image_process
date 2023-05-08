# Используйте официальный образ Python
FROM python:3.8-slim-buster

# Установите рабочую директорию
WORKDIR /app

# Копируйте файлы с зависимостями и установите их
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt --default-timeout=100

# Копируйте остальные файлы приложения
COPY . .

# Откройте порт для приложения
EXPOSE 5000

# Запустите приложение
CMD ["python", "app.py"]
