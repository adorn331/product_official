FROM python:3.5

RUN mkdir /project
WORKDIR /project
ADD requirements.txt /project

RUN pip install -r requirements.txt

ADD . /project