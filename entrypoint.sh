#!/bin/sh

echo "Applying migrations..."

python manage.py migrate --noinput

echo "Creating superuser..."

python manage.py createsuperuser --noinput || echo "Superuser already exists"

echo "Starting server..."

exec "$@"
