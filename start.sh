#!/bin/bash

# Clean up existing resources
echo "Cleaning up Docker environment..."
docker-compose down --remove-orphans
docker system prune -f
docker volume prune -f

# Build the Docker containers (with no-cache to ensure fresh builds)
echo "Building Docker containers..."
docker-compose build --no-cache

# Start the containers in detached mode
echo "Starting Docker containers..."
docker-compose up -d

# Wait a moment for the database to fully initialize
echo "Waiting for database to initialize..."
sleep 5

# Run migrations
echo "Running migrations..."
docker-compose exec web python manage.py migrate

# Collect static files (optional, uncomment if needed)
# echo "Collecting static files..."
# docker-compose exec web python manage.py collectstatic --noinput

# Open the web application in the browser (optional, uncomment if needed)
# echo "Opening the web application..."
# xdg-open http://localhost:5000  # For Linux
# open http://localhost:5000      # For macOS
# start http://localhost:5000     # For Windows (cmd)

echo "Docker containers are up and running!"