# Use the official Python image as a base
FROM  python:3.12-alpine3.20

# Set environment variables for Flask
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=5000
# Set the working directory inside the container
WORKDIR /app

# Copy the Flask application code into the container
COPY . .

# Install dependencies
RUN pip install -r requirements.txt

# Copy the Scores.txt file into the container
RUN mv scores.txt /scores.txt

# Expose the port on which the Flask app will run
EXPOSE 5000

# Command to run the Flask application
CMD ["flask", "run"]
