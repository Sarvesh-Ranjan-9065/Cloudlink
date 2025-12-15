# FROM python:3.11-slim

# WORKDIR /app

# COPY app/requirements.txt .

# RUN pip install --no-cache-dir -r requirements.txt

# COPY app/src/ .

# EXPOSE 5000

# CMD ["python", "main.py"]


FROM python:3.11-slim

WORKDIR /app

COPY app/requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY app/src/ .

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
