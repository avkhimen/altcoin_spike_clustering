FROM python:3.10-slim

RUN apt-get update
RUN apt-get upgrade
RUN apt-get install unzip zip

RUN pip install gdown

COPY ./requirements.txt .

RUN pip install -r requirements.txt

WORKDIR /home/jovyan/app

RUN mkdir /home/jovyan/app/data

CMD ["sh","run.sh"]
