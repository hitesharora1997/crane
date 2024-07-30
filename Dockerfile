# Stage 1: Build the backend
FROM python:3.9-slim as backend-build

WORKDIR /app

# Install runtime dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY backend /app/backend

# Stage 2: Final stage
FROM python:3.9-slim

WORKDIR /app

# Copy only the necessary files from the build stage
COPY --from=backend-build /app/backend /app/backend
COPY static /app/static

# Install runtime dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

CMD ["uvicorn", "backend.main:app", "--host", "0.0.0.0", "--port", "8000"]