FROM python:3.9-buster

RUN pip install wikipedia
WORKDIR /src
COPY ./src /src
ENTRYPOINT python run.py
