###
# for simplicity all dates needs to be within yyyy-mm-dd format
###

from portfolio import Portfolio
from stock import Stock
import pandas as pd
import numpy as np

# read data of stocks
data = pd.read_csv('data.csv', parse_dates=['date'])

# create stock objects
stocks = {}
for name in data['name'].unique():
    stocks[name] = Stock(name, data[data['name'] == name].copy())

# create portfolio
p = Portfolio()

# add stocks to portfolio
p.add_stock(
    stocks['AAPL'],
    20,
    np.datetime64('2000-12-24')
)
p.add_stock(
    stocks['NVDA'],
    60,
    np.datetime64('2015-07-11')
)

# get profit

initial_date = '2002-02-05'
final_date = '2002-02-25'

initial_date = np.datetime64(initial_date)
final_date = np.datetime64(final_date)

print(p.profit(initial_date, final_date))