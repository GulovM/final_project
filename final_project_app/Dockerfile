# Используем официальный минимальный образ Python 3.12.3
FROM python:3.12.3-slim

# Устанавливаем рабочую директорию в контейнере
WORKDIR /app

# Копируем файл зависимостей в рабочую директорию
COPY requirements.txt requirements.txt

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Копируем весь исходный код в рабочую директорию
COPY . .

# Открываем порт 5000 для Flask
EXPOSE 5000

# Определяем команду запуска приложения
CMD ["python", "app.py"]
