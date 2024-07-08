#!/bin/bash

# Wait for database services to be available
while ! nc -z db-timescale 5432; do
  echo "Waiting for TimescaleDB to be available..."
  sleep 0.1
done

while ! nc -z db-mongo 27017; do
  echo "Waiting for MongoDB to be available..."
  sleep 0.1
done

# Install dependencies
poetry install --no-interaction --no-ansi

# Run the development server
exec "$@"
