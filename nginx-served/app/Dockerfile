FROM ubuntu:latest

# Install Python and pip
RUN apt-get update && \
    apt-get install -y python3.10 python3-pip

# Set the working directory
WORKDIR /home/ubuntu

# Copy requirements and install dependencies
COPY src/requirements.txt .

# Install dependencies as the root user
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application files
COPY src/app01.py src/wsgi.py src/gunicorn_config.py ./

# Expose the port
EXPOSE 8080

# Switch to the non-root user
# Start Gunicorn
CMD ["gunicorn", "-c", "gunicorn_config.py", "wsgi:app"]
