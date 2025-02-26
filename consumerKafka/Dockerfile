FROM python:3.9-slim

WORKDIR /app

# Copy requirements.txt and installs
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copies rest of the files in this case it is consumer.py
COPY . .

# Turns on consumer
CMD ["python", "consumer.py"]
