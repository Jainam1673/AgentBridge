# Use a multi-stage build for a smaller image
FROM python:3.13-slim AS builder

# Set shell to bash
SHELL ["/bin/bash", "-c"]

# Install uv
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# Set working directory
WORKDIR /app

# Copy dependency files
COPY pyproject.toml uv.lock ./

# Install dependencies using uv
RUN uv sync --frozen --no-cache --no-dev

# Final stage
FROM python:3.13-slim

WORKDIR /app

# Copy the virtualenv from the builder
COPY --from=builder /app/.venv /app/.venv

# Copy the application code
COPY src /app/src
COPY migrations /app/migrations
COPY alembic.ini /app/alembic.ini

# Set environment variables
ENV PATH="/app/.venv/bin:$PATH"
ENV PYTHONUNBUFFERED=1

# Expose port
EXPOSE 8080

# Command to run the application
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8080"]
