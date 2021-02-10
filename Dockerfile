FROM python:3.8.3-alpine

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apk update

RUN apk add --virtual build-deps gcc python3-dev musl-dev \
    && apk add postgresql postgresql-dev jpeg-dev zlib-dev

RUN pip install --upgrade pip
RUN pip install pipenv

COPY ./Pipfile .
COPY ./Pipfile.lock .

RUN pipenv install
RUN apk del build-deps

# copy project
COPY . .
