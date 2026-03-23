# Event Management API

A Django REST Framework API for managing events, registrations, authentication, and API documentation.

## Overview

This project allows users to:

- create, view, update, and delete events;
- register for events;
- authenticate securely;
- search and filter events;
- access interactive API documentation.

## Features

- **Event CRUD** — full lifecycle management of events.
- **Registration System** — users can register for events with capacity validation.
- **Authentication** — JWT-based API access.
- **Email Integration** — automated notifications are sent when registrations are created, and in local development emails are logged to the console.
- **Search & Filtering** — search events by title and filter results.
- **API Documentation** — Swagger / ReDoc.
- **Testing** — automated test coverage with pytest.
- **Docker Support** — easy local setup with Docker Compose.

## Tech Stack

- Python 3.12
- Django 5.x
- Django REST Framework
- PostgreSQL
- Docker
- Docker Compose
- Ruff
- pytest-django
- pytest-cov



## Installation

### Prerequisites

- Docker
- Docker Compose
- Git

### Clone the repository
```
bash 

git clone https://github.com/SofaD8/event-management.git 
cd event-management
``` 

### Environment variables

Copy the example environment file:
```
bash 

cp .env.sample .env   # Linux/macOS
copy .env.sample .env  # Windows
``` 

Then update the values if needed.

## Run with Docker

Build and start the containers:
```
bash 

docker-compose up --build
``` 

Apply migrations:
```
bash 

docker-compose exec web python manage.py migrate
``` 

Create a superuser:
```
bash 

docker-compose exec web python manage.py createsuperuser
``` 

## Testing

Run tests:
```
bash 

docker-compose exec web pytest
``` 

Generate coverage report:
```
bash 

docker-compose exec web pytest --cov=.
``` 

Run linting:
```
bash 

docker-compose exec web ruff check .
``` 

## API Documentation

After starting the server, open:

* **Interactive API Docs (Swagger)**: [http://localhost:8000/api/docs/](http://localhost:8000/api/docs/)

## Notes

- The project is designed as a REST API.
- Docker is the recommended way to run the application locally.
- Search, filtering, and ordering are available for events.

## License

This project is provided as part of a test task.

