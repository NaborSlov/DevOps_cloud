FROM python:3.11-slim

WORKDIR /app

ENV AUTHOR="NaborSlov"
ENV UUID="f5cf8762-4829-4495-a391-b1a3fe8dad85"

COPY ./requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 8000
CMD python ./app.py
