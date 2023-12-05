FROM python:3.8-slim-buster

COPY requirements.txt .
ADD projeto_video .

RUN pip install --no-cache-dir -r requirements.txt

RUN apt-get update && \
    apt-get install -y ffmpeg