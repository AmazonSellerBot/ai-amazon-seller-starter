FROM python:3.10

WORKDIR /app

# Ensure git is available for pip if needed later
RUN apt-get update && \
    apt-get install -y git && \
    apt-get clean

COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
