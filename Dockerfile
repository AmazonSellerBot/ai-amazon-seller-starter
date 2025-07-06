# Use the official Python base image
FROM python:3.10-slim

# Set working directory inside container
WORKDIR /app

# Copy local files to the container
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Tell Railway what internal port we're listening on
EXPOSE 8000

# Launch FastAPI app directly (with hardcoded port instead of $PORT)
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
