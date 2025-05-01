#!/bin/sh

set -e

echo "⏳ Waiting for database..."

# Wait for the PostgreSQL port to open
until nc -z "${DB_HOST:-user_db}" 5432; do
  echo "⏳ PostgreSQL is unavailable - waiting..."
  sleep 1
done

echo "✅ PostgreSQL is up - running Alembic migrations..."
alembic upgrade head

echo "🚀 Starting FastAPI app..."
gunicorn -k uvicorn.workers.UvicornWorker -w "$WORKERS" -b "0.0.0.0:$PORT" app.main:app --max-requests "$MAX_REQUEST"
