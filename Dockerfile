FROM python:3.11-slim

WORKDIR /app

RUN adduser --disabled-password --gecos "" appuser

# Install only the required system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    libpq-dev \
    netcat-openbsd \
    libc6-dev \
    python3-dev \
    && rm -rf /var/lib/apt/lists/* \
    && apt-get clean

# Copy requirements first to leverage Docker cache
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY docker-entrypoint.sh .
RUN chmod +x docker-entrypoint.sh

# Copy application code last (changes most frequently)
COPY . .

RUN chown -R appuser:appuser /app

USER appuser

EXPOSE 8001

CMD ["sh", "./docker-entrypoint.sh"]