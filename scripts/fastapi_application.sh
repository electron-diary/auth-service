#!/bin/bash

# Exit on any error
set -e

# Get the directory where the script is located
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

# Define the path to gunicorn config
GUNICORN_CONFIG="${SCRIPT_DIR}/../gunicorn/config.py"

# Define the application factory path
APP_FACTORY="app.main.factories:fastapi_app_factory"

# Check if gunicorn config exists
if [ ! -f "$GUNICORN_CONFIG" ]; then
    echo "Error: Gunicorn config not found at ${GUNICORN_CONFIG}"
    exit 1
fi

# Check if gunicorn is installed
if ! command -v poetry run gunicorn &> /dev/null; then
    echo "Error: gunicorn is not installed"
    echo "Please install it using: pip install gunicorn"
    exit 1
fi

# Function to handle cleanup on exit
cleanup() {
    echo "Shutting down Gunicorn server..."
    kill -TERM $PID 2>/dev/null
}

# Set up trap for cleanup
trap cleanup SIGINT SIGTERM

# Print startup message
echo "Starting Gunicorn server..."
echo "Using config: ${GUNICORN_CONFIG}"
echo "Application factory: ${APP_FACTORY}"

# Start Gunicorn
poetry run gunicorn -c "$GUNICORN_CONFIG" "$APP_FACTORY"

# Store PID of gunicorn
PID=$!

# Wait for gunicorn to exit
wait $PID