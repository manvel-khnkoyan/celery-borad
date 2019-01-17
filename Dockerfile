FROM python:3.6

ENV PYTHONUNBUFFERED 1
ENV DOCKER_CONTAINER 1

COPY ./requirements.txt /code/requirements.txt
RUN pip install -r /code/requirements.txt

FROM ubuntu

COPY . /code/
WORKDIR /code/

RUN apt-get update

RUN apt-get  install -y npm
RUN npm install -g --no-optional pm2



EXPOSE 8000