FROM python:3.9

WORKDIR /usr/src/app

COPY . /usr/src/app

RUN python -m pip install --upgrade pip
RUN pip install pipenv
RUN pipenv install
RUN pipenv sync





