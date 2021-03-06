FROM python:3.9.1-alpine

EXPOSE 8000
WORKDIR /usr/src/news_api


ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev

RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt
RUN rm requirements.txt


COPY ./news_board .