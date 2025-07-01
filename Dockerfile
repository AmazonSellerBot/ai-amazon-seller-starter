# Use official Python image
FROM python:3.10-slim

# Install system dependencies
RUN apt-get update && apt-get install -y \
  git \
  && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy requirements
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy app code
COPY . .

# Expose the default port
EXPOSE 8000

# Start the app
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
