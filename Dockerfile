# Use official Python image as base
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Install git (in case SP-API package is pulled from GitHub)
RUN apt-get update && apt-get install -y git && apt-get clean

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip && pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application
COPY . .

# Set default port value if not defined
ENV PORT=8000

# Expose the port (important for Railway routing)
EXPOSE ${PORT}

# Launch the app correctly with evaluated port
CMD ["sh", "-c", "uvicorn app:app --host 0.0.0.0 --port ${PORT}"]

