import requests, json
from config import *
from time import sleep
# The rate limit is 200 requests per every minute per API key.

BASE_URL = 'https://paper-api.alpaca.markets'
ACCOUNT_URL = "{}/v2/account".format(BASE_URL)
ORDERS_URL = '{}/v2/orders'.format(BASE_URL)

HEADERS = {'APCA-API-KEY-ID': API_KEY, 'APCA-API-SECRET-KEY': SECRET_KEY}

def get_account():
    r = requests.get(ACCOUNT_URL, headers=HEADERS)
    return json.loads(r.content)

def create_order(symbol, qty, side, type, time_in_force):
    data = {
        "symbol": symbol,
        "qty": qty,
        "side": side,
        "type": type,
        "time_in_force": time_in_force
    }
    r = requests.post(ORDERS_URL, json=data, headers=HEADERS) # Send request to Alpaca
    return json.loads(r.content)

# API Documentation Link: https://docs.alpaca.markets/api-documentation/api-v2/
# Use third party market screeners
# https://finviz.com/screener.ashx
# https://stockfetcher.com/ 

# ORDERS: https://docs.alpaca.markets/api-documentation/api-v2/orders/
stocks = ['AAPL', 'TWTR', 'REKR']

SYMBOL = 'stock_name'
SHARES = 
BUY_OR_SELL = "buy"

# Type can be: market, limit, stop, stop_limit
TYPE = "market"

# day, gtc, opg, cls, ioc, fok
TIME_IN_FORCE = "gtc"

# Create order, don't need to save into response
response = create_order(SYMBOL, SHARES, BUY_OR_SELL, TYPE, TIME_IN_FORCE)