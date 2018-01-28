FROM python:3.6.4

WORKDIR /usr/src

COPY requirements.txt .
RUN pip install -r requirements.txt

ADD https://api.github.com/repos/conuhacks2018-mEar/ai_model/git/refs/heads/master version.json
RUN git clone https://github.com/conuhacks2018-mEar/ai_model.git app
WORKDIR /usr/src/app

COPY . .

CMD python app.py
