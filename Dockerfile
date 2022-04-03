FROM python:3.9-slim

ENV FLASK_APP app:app
WORKDIR /code
COPY requirements.txt .

RUN python -m pip install pip --upgrade pip && pip install -r requirements.txt

#CMD ["flask", "run", "-h", "0.0.0.0", "-p", "80"]