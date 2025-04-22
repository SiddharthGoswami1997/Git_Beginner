# Multi-stage build: Build stage
FROM python:3.11-alpine as builder
WORKDIR /app
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Final stage: Runtime stage
FROM python:3.11-alpine
WORKDIR /app
COPY . /app/
RUN rm -rf /var/lib/apt/lists/* /tmp/* /root/.cache
EXPOSE 8000
CMD ["python", "app.py"]
