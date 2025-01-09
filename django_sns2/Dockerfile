# syntax=docker/dockerfile:1
FROM python:3.11
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV PIP_NO_CACHE_DIR=1
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt \
    && rm -rf ~/.cache/pip/*
COPY . /code/