import pandas as pd
from alpha_vantage.timeseries import TimeSeries
import time

stock_symbol = 'TWTR'
API_KEY =  'ZR3YX9P081EYTXEK'

ts = TimeSeries(key=API_KEY, output_format='pandas')

data, meta_data = ts.get_intraday(symbol=stock_symbol, interval='1min', outputsize='full')

print(data)