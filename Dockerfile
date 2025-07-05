# Use official Python image as base
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Install git
RUN apt-get update && apt-get install -y git && apt-get clean

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip && pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application
COPY . .

# Make sure start.sh is executable
RUN chmod +x ./start.sh

# Set default port value if not defined
ENV PORT=8000

# Expose the port for Railway
EXPOSE $PORT

# ✅ Use the script as the CMD
CMD ["./start.sh"]
