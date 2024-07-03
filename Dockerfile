# Use a Python runtime as a base image
FROM python:3.9-alpine

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set working directory in the container
WORKDIR /app

# Copy and install requirements
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY . /app

# Create a volume for data (if needed)
VOLUME /app/data

# Expose port 5000
ENV PORT 5000
EXPOSE $PORT

# Define the command to run the application using Gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:$PORT", "app:app"]
