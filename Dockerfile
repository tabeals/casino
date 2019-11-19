FROM python:2.7-alpine
MAINTAINER ta thomasbeals

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt


WORKDIR /home/tabeals/code/casino
COPY ./casino /casino

RUN adduser -D tabeals
USER tabeals
