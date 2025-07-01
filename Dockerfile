# Use an official Python image
FROM python:3.10-slim

# Install git for cloning SP-API package
RUN apt-get update && apt-get install -y git && apt-get clean

# Set work directory
WORKDIR /app

# Copy requirements first for caching
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the app
COPY . .

# Run the FastAPI app with Uvicorn
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
