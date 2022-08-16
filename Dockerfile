FROM python:3.9-alpine
ENV PYTHONUNBUFFERED 1

WORKDIR /portfolio

COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .   
CMD python manage.py runserver localhost:80