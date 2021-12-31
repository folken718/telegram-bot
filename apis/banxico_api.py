import os
from dotenv import load_dotenv
import requests

# Loading .env variables
load_dotenv()

# Getting .env variables
TOKEN = os.getenv('BANXICO_TOKEN')

banxicoUrl = 'https://www.banxico.org.mx/SieAPIRest/service/v1/series/SF60653/datos'

params = {'token': TOKEN}
exchangeRateRaw = requests.get(banxicoUrl, params=params)
exchangeRate = exchangeRateRaw.json()


def normilizeData(rawData):
    dataDictionary = {}
    for item in rawData:
        dataDictionary[item['fecha']] = item['dato']
    return dataDictionary


rawData = exchangeRate['bmx']['series'][0]['datos']
goodData = normilizeData(rawData)

print(goodData)
