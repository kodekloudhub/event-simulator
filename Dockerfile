FROM python:alpine

RUN mkdir /log

ADD event-simulator.py .

ENTRYPOINT python event-simulator.py