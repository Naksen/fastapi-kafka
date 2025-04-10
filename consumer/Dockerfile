FROM python:3.12-slim

RUN pip install poetry

WORKDIR /app

RUN pip install fastapi[standard] uvicorn faststream[kafka]

COPY . /app/
COPY ./certs /certs