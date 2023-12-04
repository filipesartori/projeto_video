FROM python:3.8-slim-buster

COPY requirements.txt .
ADD projeto_video .

RUN pip install -r requirements.txt