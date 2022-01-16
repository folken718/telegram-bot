import os
from dotenv import load_dotenv
import requests
from functools import lru_cache
from datetime import datetime


# Loading .env variables
load_dotenv()

# Getting .env variables
TOKEN = os.getenv('EXCHANGE_TOKEN')

exchange_url = f'http://api.exchangeratesapi.io/v1/latest?access_key={TOKEN}'

params = {'token': TOKEN}

currency = {'usd': 'usd', 'cad': 'cad'}


def get_day_exchange_rate():
    exchangeRateRaw = requests.get(exchange_url)
    exchangeRate = exchangeRateRaw.json()
    ratesDict = exchangeRate['rates']
    return ratesDict


def get_today_dollar_exchange_rate(dollar_type):
    ratesDict = get_day_exchange_rate()
    mxn_cad = ratesDict['MXN']/ratesDict['CAD']
    mxn_usd = ratesDict['MXN']/ratesDict['USD']
    rate = mxn_usd if dollar_type == 'usd' else mxn_cad
    return "{:.2f}".format(rate)


@lru_cache(15)
def get_today_exchange_rate(currency_type, date):
    today_rate = get_today_dollar_exchange_rate(currency_type)
    msg = f'Today - {date}, {currency_type} exchange rate is {today_rate}'
    return msg


# today = datetime.today().strftime('%d/%m/%Y')
# print(get_today_exchange_rate('usd', today))
