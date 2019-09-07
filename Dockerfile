FROM python:3.7-slim

WORKDIR /usr/app

ENV FLASK_APP ./src/app.py
ENV FLASK_RUN_HOST 0.0.0.0

COPY . .

RUN python -m venv venv && \
	. venv/bin/activate && \
	pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

CMD . venv/bin/activate && \
	flask run
