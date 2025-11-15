#!/usr/bin/env bash
# Exit on error
set -o errexit

# Install dependencies
pip install -r requirements.txt

# Run collectstatic (this will find the command now)
python manage.py collectstatic --noinput

# Run database migrations
python manage.py migrate