# Use official Python base image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy all files
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Set environment variable for Railway
ENV PORT=8000

# Expose the port
EXPOSE 8000

# Run the app with uvicorn (Railway will map the internal port)
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
