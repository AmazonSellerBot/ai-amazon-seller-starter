# Use an official Python base image
FROM python:3.10-slim

# Set the working directory
WORKDIR /app

# Install system dependencies (e.g., git if needed)
RUN apt-get update && apt-get install -y git && apt-get clean

# Copy and install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip && pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Expose port 8000
EXPOSE 8000

# Start the FastAPI app using uvicorn
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
