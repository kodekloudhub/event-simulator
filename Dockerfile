FROM python:alpine

ADD event-simulator.py .

ENTRYPOINT python event-simulator.py