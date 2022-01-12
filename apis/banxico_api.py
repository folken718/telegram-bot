import os
from dotenv import load_dotenv
import requests
from functools import lru_cache
from datetime import datetime


# Loading .env variables
load_dotenv()

# Getting .env variables
TOKEN = os.getenv('BANXICO_TOKEN')

banxicoUrl = 'https://www.banxico.org.mx/SieAPIRest/service/v1/series/SF60653/datos'

params = {'token': TOKEN}

@lru_cache
def get_exchange_rate_history_baxico():
    exchangeRateRaw = requests.get(banxicoUrl, params=params)
    exchangeRate = exchangeRateRaw.json()
    return exchangeRate;


def normilizeData(rawData):
    dataDictionary = {}
    for item in rawData:
        dataDictionary[item['fecha']] = item['dato']
    return dataDictionary

def get_exchange_rate_from_date(date):
    exchangeRate = get_exchange_rate_history_baxico()
    dataDictionary = normilizeData(exchangeRate['bmx']['series'][0]['datos'])
    return dataDictionary[date]

today = datetime.today().strftime('%d/%m/%Y')
print(get_exchange_rate_from_date(today))
