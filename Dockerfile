# Use the official Python 3.8 slim image as the base image
FROM python:3.8-slim

# Set the working directory within the container
WORKDIR /src/

COPY app /src/

COPY requirements.txt /src/

# Upgrade pip and install Python dependencies
RUN pip3 install --upgrade pip && pip install --no-cache-dir -r requirements.txt

# Expose port 5000 for the Flask application

# Define the command to run the Flask application using Gunicorn
CMD ["gunicorn", "main:app", "-b", "0.0.0.0:5000", "-w", "4", "--reload"]
