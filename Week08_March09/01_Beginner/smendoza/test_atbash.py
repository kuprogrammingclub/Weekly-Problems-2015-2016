'''
test_atbash.py

Author: Stefan Mendoza
Date: 13 March 2016

Test suite for Atbash cipher implementation.
'''

from atbash import cipher
import nose

def test_cipher_one():
    assert cipher("foobar") == "ullyzi"

def test_cipher_two():
    assert cipher("wizard") == "draziw"

def test_cipher_three():
    assert cipher("/r/dailyprogrammer") == "/i/wzrobkiltiznnvi"

def test_cipher_four():
    assert(cipher("gsrh rh zm vcznkov lu gsv zgyzhs xrksvi") ==
                  "this is an example of the atbash cipher")
