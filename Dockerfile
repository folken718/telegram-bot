FROM python:3.10.2-slim-bullseye
WORKDIR /usr/app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .
CMD [ "python", "basic_bot.py" ]
