# Use official Python image as base
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Install git
RUN apt-get update && apt-get install -y git && apt-get clean

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip && pip install --no-cache-dir -r requirements.txt

# Copy app files
COPY . .

# Set static port and expose
ENV PORT=8000
EXPOSE 8000

# Run FastAPI app directly
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
