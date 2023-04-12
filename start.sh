#!/bin/bash
# Collect project static.
python src/manage.py collectstatic --noinput --clear

# Start project containers.
docker-compose build
docker-compose up -d