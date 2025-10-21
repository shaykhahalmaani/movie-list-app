FROM python:3.10-slim

WORKDIR /app

# Install pip and flask
RUN pip install flask flask-cors

# Copy application code
COPY . .

# Expose port
EXPOSE 5000

# Run the application
CMD ["python", "app.py"]
