#!usr/bin/env python3

'''
stock_market.py

Author: Stefan Mendoza
Date: 4 February 2016

Given a list of space-delimited stock prices, etermines the price to buy and
sell price of two trades.

Restrictions
- The buy and sell trades have to be at least one trade apart
'''

file_name = input('Enter a file name in this directory: ')

data = [float(i) for i in open(file_name, 'r').read().split()]

low = data[0]
low_index = 0
high = -1
high_index = -1

for i in range(0, len(data)):
    if data[i] < low and (high - data[i] > high - low):
        low = data[i]
        low_index = i
        high = -1
        high_index = -1
    if data[i] > high and (data[i] - low) > (high - low) and i - low_index > 1:
        high = data[i]
        high_index = i

print(low, high)
