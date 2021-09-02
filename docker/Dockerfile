FROM python:3.8.10

WORKDIR /usr/src/app

COPY .. /usr/src/app

RUN python -m pip install --upgrade pip
RUN pip install pipenv
RUN pipenv install
RUN pipenv sync





