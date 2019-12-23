import csv
from collections import defaultdict

open_prices = []

####################
# Getting Data     #
####################
with open('TWTR.csv') as csv_file:
  csv_reader = csv.reader(csv_file, delimiter=',')
  next(csv_reader)
  for row in csv_reader:
    open_prices.append(float(row[1]))

prices = {}

starting_capital = float(input("Enter starting capital: "))

for price in open_prices:
  if price not in open_prices:
    prices[int(price)] = 0
  else:
    prices[int(price)] = prices.get(int(price), 0) + 1

resistance_price = max(prices, key=prices.get)
support_price = min(prices, key=prices.get)

####################
# Begin simulation #
####################
total_shares = 0
shares = 30
profit_loss = 0
total_investment = 0
total_proceeds = 0
profit_loss_percentage = 0

for price in open_prices:
  # Buy shares if the price goes past the resistance line
  # Make sure that we still have at least $2,000 leftover
  if price >= resistance_price and starting_capital >= 2000:
    # Get the total shares
    total_shares += shares
    # Calculate the total investment
    total_cost = price * shares
    print(f'Buying {shares} @ {price} for a total cost of {total_cost}')
    total_investment = total_cost
    # Subtract from capital
    starting_capital -= total_investment
    print(f'Current Capital: {starting_capital}')
  elif price > support_price and price < resistance_price: # If the price goes below the resistance
    print(f'Before selling, we had  {total_shares} shares')
    # Sell all the shares
    total_shares -= total_shares
    # Calculate the profit/loss
    profit_loss = total_investment - (price * shares)
    starting_capital += profit_loss
    print(f'Selling all shares, the current total shares is {total_shares}  @ {price}')
    print(f'Profit/Loss: {profit_loss}')

print(f'The resistance price was: {resistance_price}')
print(f'The support price was: {support_price}')
print(f'Remaining capital: {starting_capital}')
print(f'Total Investment: {total_investment}')
print(f'Profit/Loss: {profit_loss}')