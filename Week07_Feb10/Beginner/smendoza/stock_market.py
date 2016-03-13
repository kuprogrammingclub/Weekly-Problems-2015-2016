#!usr/bin/env python3

'''
stock_market.py

Author: Stefan Mendoza
Date: 4 February 2016

Given a list of space-delimited stock prices, determines the price to buy and
sell price of two trades.

Restrictions
- The buy and sell trades have to be at least one trade apart
'''

import sys

def analyze(data):
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

    if high < low:
        return "No trades possible"
    else:
        return str(low) + " " + str(high)

if __name__ == "__main__":
    if sys.argv[0] == "stock_market.py" and len(sys.argv) > 1:
        data = [float(i) for i in open(sys.argv[1], 'r').read().split()]
        print(analyze(data))
