FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --upgrade pip && \
    pip install -r requirements.txt && \
    # Force correct versions to prevent urllib3 crash
    pip install urllib3==1.26.15 botocore==1.29.96 boto3==1.26.96

COPY . .

CMD ["python", "main.py"]
