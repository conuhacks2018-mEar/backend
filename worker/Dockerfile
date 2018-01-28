FROM python:3.6.4

WORKDIR /usr/src

COPY requirements.txt .
RUN pip install -r requirements.txt

RUN git clone https://github.com/conuhacks2018-mEar/ai_model.git app
WORKDIR /usr/src/app

COPY . .

CMD python app.py
