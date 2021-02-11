FROM python:3.8.3-alpine

RUN mkdir /usr/src/app
WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV LANG C.UTF-8
ENV DEBIAN_FRONTEND=noninteractive

ENV PORT=8000

RUN apk update

RUN apk add --virtual build-deps gcc python3-dev musl-dev \
    && apk add postgresql postgresql-dev jpeg-dev zlib-dev

RUN pip3 install --upgrade pip
RUN pip3 install pipenv

COPY ./Pipfile .
COPY ./Pipfile.lock .

RUN pipenv install --skip-lock --system --dev
RUN apk del build-deps
RUN apk --no-cache add musl-dev linux-headers g++

COPY . .

CMD gunicorn --bind 0.0.0.0:$PORT uks.wsgi
