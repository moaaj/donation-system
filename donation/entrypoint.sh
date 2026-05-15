#!/usr/bin/env bash
set -euo pipefail
cd /app
python manage.py migrate --noinput
exec gunicorn donation.wsgi:application --bind "0.0.0.0:${PORT:-8000}" --workers "${WEB_CONCURRENCY:-2}"
