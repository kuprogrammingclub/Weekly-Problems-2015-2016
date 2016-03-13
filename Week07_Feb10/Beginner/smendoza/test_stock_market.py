'''
test_stock_market.py

Author: Stefan Mendoza
Date: 13 March 2016

Test suite for stock_market.py
'''

from stock_market import analyze
import nose

def test_one():
    data = [float(i) for i in open('input1.txt', 'r').read().split()]
    assert analyze(data) == "18.88 19.03"

def test_two():
    data = [float(i) for i in open('input2.txt', 'r').read().split()]
    assert analyze(data) == "8.03 9.34"
#
def test_three():
    data = [float(i) for i in open('input3.txt', 'r').read().split()]
    assert analyze(data) == "No trades possible"

def test_four():
    data = [float(i) for i in open('input4.txt', 'r').read().split()]
    assert analyze(data) == "No trades possible"
