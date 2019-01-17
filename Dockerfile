FROM python:3.6

ENV PYTHONUNBUFFERED 0
ENV DOCKER_CONTAINER 1

COPY ./requirements.txt /code/requirements.txt
RUN pip install -r /code/requirements.txt

FROM ubuntu

COPY . /code/
WORKDIR /code/

RUN apt-get update

RUN apt-get  install -y npm
RUN npm install -g --no-optional pm2

WORKDIR  /home/hovo/python-files/job-management-system/

COPY process.json /home/hovo/python-files/job-management-system

CMD ["pm2-runtime", "process.json"]
 
EXPOSE 8000



#WORKDIR  /home/hovo/python-files/job-management-system/app

#COPY app.py /home/hovo/python-files/job-management-system

#CMD ["python3", "-u","/home/hovo/python-files/job-management-system/app.py"]
