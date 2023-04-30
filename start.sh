#!/bin/bash
# Stop and destroy containers.
docker-compose down
# Build and start containers.
docker-compose build
docker-compose up -d