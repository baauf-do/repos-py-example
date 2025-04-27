# Dockerfile

FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy files
COPY . .

# Install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Expose port
EXPOSE 8901

# Run app
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8901", "--reload"]
