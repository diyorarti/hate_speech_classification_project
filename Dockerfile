# --- Base Image -----
FROM python:3.11-slim 

# working directory 
WORKDIR /app

# copying dependency files
COPY requirements.txt

# installing dependency
RUN pip install --no-cache-dir -r requirements.txt

# copying project source code

COPY . .

# setting enviroment variables
ENV PYTHONDONTWRITEBYTECODE=1    #preventing Python form writing .pyc files
ENV PYTHONUNBUFFERED=1 #preventing output buffering 

# export port
EXPOSE 8080

# running API
CMD ["uvicorn", "api.main:app", "--host", "0.0.0.0", "-port", "8000"]