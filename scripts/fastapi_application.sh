#!/bin/bash

# Exit on any error
set -e

# Get the directory where the script is located

# Define the path to gunicorn config
GUNICORN_CONFIG="../gunicorn/config.py"

# Define the application factory path
APP_FACTORY="app.main.factories:fastapi_app_factory"

# Check if gunicorn config exists
if [ ! -f "$GUNICORN_CONFIG" ]; then
    echo "Error: Gunicorn config not found at ${GUNICORN_CONFIG}"
    exit 1
fi

if ! command -v gunicorn &> /dev/null; then
    echo "Error: gunicorn is not installed"
    echo "Please install it using: pip install gunicorn"
    exit 1
fi

# Print startup message
echo "Starting Gunicorn server..."
echo "Using config: ${GUNICORN_CONFIG}"
echo "Application factory: ${APP_FACTORY}"

# Start Gunicorn
gunicorn -c gunicorn -c "$GUNICORN_CONFIG" "$APP_FACTORY"
