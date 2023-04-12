FROM python:3.11-alpine

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /test_constructor/src/

RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY . ..

RUN python manage.py makemigrations
RUN python manage.py migrate --noinput
RUN python manage.py collectstatic --noinput --clear
RUN python manage.py fill_db