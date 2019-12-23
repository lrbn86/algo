import csv
from collections import defaultdict

open_prices = []

####################
# Getting Data     #
####################

# row[0] = Date
# row[1] = Open Price
# row[2] = High Price
# row[3] = Low Price
# row[4] = Close Price
# row[5] = Adjusted Close Price
# row[6] = Volume

with open('REKR.csv') as csv_file:
  csv_reader = csv.reader(csv_file, delimiter=',')
  next(csv_reader)
  for row in csv_reader:
    open_prices.append(float(row[1]))

prices = {}

starting_capital = float(input("Enter starting capital: "))

# Calculate resistance price and support price
# TODO: Find a better way to calculate these prices
for price in open_prices:
  if price not in open_prices:
    prices[int(price)] = 1
  else:
    prices[int(price)] = prices.get(int(price), 0) + 1

resistance_price = max(prices, key=prices.get)

# If the current stock price goes above the resistant price
support_price = min(prices, key=prices.get)

####################
# Begin simulation #
####################
total_shares = 0
shares = 30

# if volume >= 10000
#   shares = .1 * total_volume
# else shares = 

# volume
float
for price in open_prices:
  shares = 

# Top 6 filtered by a screener
["GOOM", "uyi", "yi", "GOO"]


# Calculating pivot points
