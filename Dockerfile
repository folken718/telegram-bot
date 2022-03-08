FROM python:3.9.10-slim-bullseye
WORKDIR /usr/app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .
ENV BOT_TOKEN=BOT_TOKEN
ENV EXCHANGE_TOKEN=EXCHANGE_TOKEN
CMD [ "python", "basic_bot.py" ]
