# Start from a lightweight Python base image
FROM python:3.9-slim

# Install the system library needed by scikit-learn/lightgbm for optimal performance
RUN apt-get update && apt-get install -y libgomp1

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file first and install dependencies
# This leverages Docker's layer caching
COPY ./requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your application code and models
COPY ./src /app/src
COPY ./models /app/models

# Expose the port the API will run on
EXPOSE 8000

# The command to start the Uvicorn server when the container launches
# The host 0.0.0.0 makes it accessible from outside the container
CMD ["uvicorn", "src.api:app", "--host", "0.0.0.0", "--port", "8000"]