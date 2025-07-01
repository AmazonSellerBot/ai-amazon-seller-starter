FROM python:3.10-slim

# Install git so we can clone the SP-API repo
RUN apt-get update && apt-get install -y git && apt-get clean

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
