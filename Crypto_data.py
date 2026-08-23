#Import libraries
import pandas as pd
import numpy as np

#Making the data
raw_data ={
    'BTC':62842,
    'ETH':1877,
    'ADA':0.1792,
    'AMZN':262,
    'TSLA':342,
    'APPL':306}
stock_prices = pd.Series(data=raw_data)
print(f'Stock prices:\n{stock_prices}')

#Making my portfolio
raw_data = {
    'BTC' : 3,
    'ETH' : 10,
    'ADA' : 1000,
    'AMZN' : 20,
    'TSLA' : 20,
    'APPL' : 5}
my_portfolio = pd.Series(data=raw_data)
print(f'My portfolio:\n{my_portfolio}')

#Obtaining the total value of my portfolio
print('Total value of my portfolio:',(my_portfolio*stock_prices).sum())

#Convert csv to Pandas Series
prices_series = pd.read_csv('S&P500_Prices.csv').squeeze()
print(f'Data t"prices_series": {type(prices_series)}')
print(f'Prices_series:\n{prices_series.head()}')

#Get the maximum, minimun and average from 'prices_series'
print('Maximum value:',prices_series.max())
print('Minimum value:',prices_series.min())
print('Average of the serie:',prices_series.mean())

#Sorting 'prices_series' in an ascending and descending order
prices_series.sort_values(ascending=True,inplace=True)
print(f'Sort by ascending order:\n{prices_series.head()}')
prices_series.sort_values(ascending=False,inplace=True)
print(f'\nSort by descending order:\n{prices_series.head()}')

#get statistical data of 'prices_series' with describe method
prices_series.describe()

#Find a price with and without rounding the series
print(f'Finding "3349" without rounding the series:',3349 in prices_series.values)
prices_series = round(prices_series)
print(f'Finding "3349" with rounding the series:',3349 in prices_series.values)
