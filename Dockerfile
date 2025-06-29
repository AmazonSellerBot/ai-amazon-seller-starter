FROM python:3.10-slim

WORKDIR /app

COPY . .

# Install git (required for installing from GitHub)
RUN apt-get update && apt-get install -y git

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "3000"]
