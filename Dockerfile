# Start from a Python 3.8 base image
FROM python:3.8-slim-buster

# Set the working directory in the Docker container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt requirements.txt

# Install the Python dependencies
RUN pip install -r requirements.txt

# Copy the .env file and your Python script into the container
COPY .env .env
COPY bot_rekviz.py bot_rekviz.py

# Set the command to run when the container starts
CMD [ "python", "./bot_rekviz.py" ]
