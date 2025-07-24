# Use Alpine-based Python image
FROM python:3.12-alpine

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set working directory
WORKDIR /app

# Copy app source
COPY . .

# Install dependencies
RUN apk add --no-cache gcc musl-dev libffi-dev \
    && pip install --no-cache-dir flask \
    && apk del gcc musl-dev libffi-dev

# Expose port
EXPOSE 5000

# Run the Flask app
CMD ["python", "app.py"]
