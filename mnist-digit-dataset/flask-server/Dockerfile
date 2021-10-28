FROM python:3.8.0-slim AS build
RUN apt-get clean && \
    apt-get update -y 

WORKDIR /build
COPY requirements.txt .
ENV PATH=/root/.local/bin:$PATH
RUN pip3 install --user --upgrade pip
RUN pip3 install --user -r requirements.txt
COPY /code ./code
CMD FLASK_APP=./code/app.py flask run --host=0.0.0.0