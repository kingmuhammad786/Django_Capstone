# Use an official Python runtime as the base image
FROM python:3.11-slim

# Environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Upgrade pip with the break-system-packages flag
RUN pip install --upgrade pip --break-system-packages

# Set working directory
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt --break-system-packages

# Copy the rest of your application code
COPY . /app/

# Expose the port on which Django runs
EXPOSE 8000

# Run Django migrations then start the development server
CMD ["sh", "-c", "python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]

