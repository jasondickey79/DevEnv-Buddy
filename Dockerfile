# Use official python image as base
FROM python:3.10-slim

# set the qorking directory in the container
WORKDIR /app

# Copy everything from current project into the container
COPY . . 

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Default command to run the app
CMD ["python", "-m", "devenvbuddy/main.py"]


