FROM python:3.12-slim

# Налаштування середовища
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    POETRY_VERSION=2.0.0 \
    POETRY_VIRTUALENVS_CREATE=false \
    POETRY_NO_INTERACTION=1

WORKDIR /app

# Встановлення системних залежностей для psycopg2 та curl
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Встановлення Poetry
RUN curl -sSL https://install.python-poetry.org | python3 -
ENV PATH="/root/.local/bin:$PATH"

# Копіюємо файли залежностей
COPY pyproject.toml poetry.lock /app/

# Встановлюємо залежності через poetry
RUN poetry install --no-root

# Копіюємо весь проект
COPY . /app/

# Команда для запуску (з автоматичною міграцією)
CMD ["sh", "-c", "python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]
