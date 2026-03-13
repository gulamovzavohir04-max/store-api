#!/bin/sh

echo "Apply database migrations"
python manage.py migrate

echo "Create superuser if not exists"
python manage.py createsuperuser --noinput || true

echo "Collect static files"
python manage.py collectstatic --noinput

echo "Start server"
gunicorn config.wsgi:application --bind 0.0.0.0:$PORT