# Base image for dependencies
FROM python:3.11-slim AS base

# Set environment variables
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

# Set working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# API Target
FROM base AS api

# Set working directory
WORKDIR /app

ENV PYTHONPATH=/app/src

CMD ["python", "src/cmd/api/main.py"]

# Book Enrichment Consumer Target
# FROM base AS book_enrichment_consumer
# CMD ["python", "cmd/book_enrichment_consumer/main.py"]
