FROM python:3.8-slim-buster

ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get install -y \
    build-essential \
    python3-dev \
    libpq-dev

RUN mkdir /app
COPY . /app/
WORKDIR /app

RUN pip install --upgrade pip
RUN pip install pipenv && pipenv install --deploy --system --ignore-pipfile
RUN useradd -s /bin/bash admin
USER admin