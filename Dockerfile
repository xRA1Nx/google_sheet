# syntax=docker/dockerfile:1
FROM python:3
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /app
COPY req.txt .
RUN pip install -r req.txt
COPY . .
EXPOSE 8000

#RUN python manage.py makemigrations
#RUN python manage.py migrate