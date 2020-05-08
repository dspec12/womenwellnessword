FROM python:3.8-slim-buster

ENV PYTHONUNBUFFERED 1

# RUN apt-get update -y && apt-get upgrade -y 

RUN mkdir /app
COPY . /app/
WORKDIR /app

RUN pip install --upgrade pip
RUN pip install pipenv && pipenv install --deploy --system --ignore-pipfile

RUN useradd -s /bin/bash admin
USER admin