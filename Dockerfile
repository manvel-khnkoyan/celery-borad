FROM ubuntu
RUN apt-get update

RUN apt-get install -y python3

ENV PYTHONUNBUFFERED 0
ENV DOCKER_CONTAINER 1

COPY ./requirements.txt /code/requirements.txt
RUN apt-get install -y python3-pip
RUN pip3 install --upgrade pip
RUN pip3 install -r /code/requirements.txt

COPY . /code/
WORKDIR /code/

RUN apt-get  install -y npm
RUN npm install -g --no-optional pm2
RUN pm2 update
#CMD ["pm2-runtime",  "process.json"]

EXPOSE 8000
