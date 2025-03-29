# Python image
FROM python:3.11

# Working directory
WORKDIR /app

# Copy requirements 
COPY requirements.txt .

# install dependesies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire application
COPY . .

# FastAPI port
EXPOSE 8000

# Run the fastapi app
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
