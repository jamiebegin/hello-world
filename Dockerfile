# Start from a lightweight Python image
FROM python:3.13-slim

RUN python3 -m venv env
RUN source ./env/bin/activate
# Set the working directory
WORKDIR /app

# Copy requirements first (for efficient caching)
COPY requirements.txt /app

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . /app

# Expose the port on which Gunicorn will listen
EXPOSE 5000

# Run Gunicorn to serve the Flask WSGI application
# Here, we point Gunicorn to the app factory function 'create_app' in 'app/__init__.py'
# by referencing it through 'main:create_app()'.
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "main:create_app()"]

