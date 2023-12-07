FROM python:3.8-slim-buster

RUN apt-get update && apt-get install -y ffmpeg

COPY requirements.txt .

RUN pip install -r requirements.txt