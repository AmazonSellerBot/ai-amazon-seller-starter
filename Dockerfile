FROM python:3.10-slim
WORKDIR /app
RUN apt-get update && apt-get install -y git && apt-get clean
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip && pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 8000
CMD uvicorn app:app --host 0.0.0.0 --port $PORT
