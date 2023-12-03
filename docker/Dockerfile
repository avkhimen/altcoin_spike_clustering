FROM python:3.10-slim

RUN apt-get update
RUN apt-get upgrade
RUN apt-get install unzip zip

COPY ./requirements.txt .

RUN pip install -r requirements.txt

WORKDIR /home/jovyan/app

#CMD ["sh","run.sh"]
