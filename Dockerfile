# Use an official Python runtime as a base image
FROM python:3.10.12
ENV PYTHONUNBUFFERED=1
# Set the working directory in the container
WORKDIR /app

# Copy requirements and install dependencies
COPY ./app/my-app/requirements.txt /app
COPY ./app/my-app/main.py /app
RUN pip install --no-cache-dir -r requirements.txt


# Expose the port your app runs on
#EXPOSE 8000

# Command to run the application
#CMD ["python", "main.py"]
