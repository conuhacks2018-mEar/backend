FROM python:3.6.4

WORKDIR /usr/src/app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY app.py .

CMD FLASK_APP=app.py flask run --host 0.0.0.0
