FROM python:3.10

WORKDIR /app

RUN apt-get update && \
    apt-get install -y git && \
    apt-get clean

COPY requirements.txt .

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "${PORT}"]
