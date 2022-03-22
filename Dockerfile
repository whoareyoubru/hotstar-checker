FROM python:3.10-slim-buster
RUN apt-get update -y && apt-get upgrade -y
RUN apt-get install python3-pip -y
COPY . /app/
RUN chmod 777 /app/
WORKDIR /app/
RUN python3 -m pip install --no-cache-dir -r req*
RUN python3 bot.py
