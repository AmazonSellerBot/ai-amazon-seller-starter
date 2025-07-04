# Use an official Python image as the base
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Install system packages (if needed, e.g., git for pip installs from GitHub)
RUN apt-get update && apt-get install -y git && apt-get clean

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip && pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Expose port 8000 for clarity (optional for Railway)
EXPOSE 8000

# Use the PORT variable (important for Railway)
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "${PORT}"]
