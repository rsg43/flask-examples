FROM mcr.microsoft.com/devcontainers/python:1-3.12-bookworm

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN apt update && apt upgrade -y
RUN apt install python3-enchant aspell aspell-en -y

COPY requirements.txt .
RUN pip install -r requirements.txt

WORKDIR /app
COPY . /app
