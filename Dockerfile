FROM python:3.6.4

WORKDIR /usr/src/app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .
RUN pip install -e .

ENV FLASK_APP=backend
CMD flask run --host 0.0.0.0
