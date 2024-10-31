#!/bin/bash

# Exit immediately if a command exits with a non-zero status
set -e

# Define the path to alembic.ini
ALEMBIC_CONFIG="../alembic.ini"

# Check if alembic.ini exists
if [ ! -f "$ALEMBIC_CONFIG" ]; then
    echo "Error: alembic.ini not found at ${ALEMBIC_CONFIG}"
    exit 1
fi

# Run the migration
echo "Running database migration..."
alembic -c "$ALEMBIC_CONFIG" upgrade 022e9b18d152

# Check if the migration was successful
if [ $? -eq 0 ]; then
    echo "Migration completed successfully"
else
    echo "Migration failed"
    exit 1
fi