#!/usr/bin/env bash
set -e

echo "Running database migrations..."
python manage.py migrate --noinput

echo "Seeding product categories and products..."
python manage.py seed_products

echo "Collecting static files..."
python manage.py collectstatic --noinput --clear

echo "Starting Gunicorn..."
exec gunicorn apextrail_proj.wsgi:application --bind 0.0.0.0:${PORT:-8000}
