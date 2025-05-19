# Use an official Python runtime as a parent image
FROM python:3.13

# Set the working directory
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire Django project into the container
COPY . .

# Set environment variables
ENV DJANGO_SETTINGS_MODULE=portfolio_project.settings
ENV PYTHONUNBUFFERED=1

# Run migrations and collect static files
RUN python manage.py migrate && python manage.py collectstatic --noinput

# Expose port 8000 for Django
EXPOSE 8000

# Run the Django server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
