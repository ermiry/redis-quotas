FROM python:3.9.2-slim-buster

WORKDIR /home/auth

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

CMD ["python3", "-u", "service/app.py"]
