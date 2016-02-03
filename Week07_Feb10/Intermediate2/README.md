## Intermediate 2 - Roman Numeral Conversion
__Source__: http://bit.ly/1mdqOf8

Most people learn about roman numerals at a young age. If you look at many
analog clocks, you will find that many of them actually use roman numerals for
the numbers. Roman numerals do not just stop at 12 though, they actually can
represent numbers as high as 4999 using their most basic form. The challenge is
to create a program that will allow you to convert decimal (base-10) numbers to
roman numerals as well as roman numerals to decimal numbers. The history of
roman numerals is a bit debated because of their varied use throughout history
and a seeming lack of a standard definition. Some rules are well accepted and
some less-so. Here are the guidelines for your implementation:

* I = 1
* V = 5
* X = 10
* L = 50
* C = 100
* D = 500
* M = 1000


#### Rules

You cannot repeat the same roman numeral more than three times in a row, except
for M, which can be added up to four times. (Note: Some descriptions of roman
numerals allows for IIII to represent 4 instead of IV. For the purposes of
this exercise, that is not allowed.) When read from left to right, if successive
roman numerals decrease or stay the same in value, you add them to the total sum.
When read from left to right, if successive roman numerals increase in value,
you subtract the smaller value from the larger one and add the result to the
total sum.


#### Constraints

I can only be subtracted from V or X
X can only be subtracted from L or C
C can only be subtracted from D or M

Only one smaller value can be subtracted from a following larger value.
(e.g. 'IIX' would be an invalid way to represent the number 8)


#### Examples
```
XII = 10 + 1 + 1 = 12
MDCCLXXVI = 1000 + 500 + 100 + 100 + 50 + 10 + 10 + 5 + 1 = 1776
IX = "1 from 10" = 10 - 1 = 9
XCIV = "10 from 100" + "1 from 5" = (100 - 10) + (5 - 1) = 90 + 4 = 94
```
