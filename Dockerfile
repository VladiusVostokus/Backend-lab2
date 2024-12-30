FROM python:3.11.3-slim-bullseye

WORKDIR /app

COPY requirements.txt .

RUN python -m pip install -r requirements.txt

RUN python -m pip install flask

COPY . /app

CMD flask --app src/app run -h 0.0.0.0 -p $PORT