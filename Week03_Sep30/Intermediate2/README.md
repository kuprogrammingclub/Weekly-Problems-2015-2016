## Intermediate 2 - Hyperbinary Computation
__*Source*__: https://www.reddit.com/r/dailyprogrammer/comments/2xx86n/20150302_challenge_204_intermediate_its_like/

Imagine that instead of having just the two digits 0 and 1, the binary number system
had three digits, 0, 1 and 2 with everything else working exactly the same. This
system is known as the "hyperbinary number system". <br>

Lets see an example how the hyperbinary number system works. Lets take the
hyperbinary number "1021", and try and figure out what number it represents.
ust as before, each position represents a power of 2, but now you can have 0,
1 or 2 of each of them, so the calculation goes like this:

<br>
1 \* 2 <sup>3</sup> + 0 \* 2<sup>2</sup> + 2 \* 2<sup>1</sup> + 1 \* 2<sup>0</sup><br>
= 8 + 2 \* 2 + 1<br>
= 8 + 4 + 1<br>
= 13
<br>

Interestingly, this is not the only way you can represent the number 13 in hyperbinary, you could also write 13 as "221" and "1101".<br>

In fact, this is a common issue with this number system: most numbers can be written in multiple ways in hyperbinary. Your challenge today is to find every single hyperbinary representation of a given number.

#### Input
The input will be a single line containing a single number (written in regular decimal).

#### Output
Your program should print out all possible representations of the input number
in hyperbinary, one per line. Every representation should be printed out once
and only once. The order of the outputs doesn't matter, and you can use leading
zeroes if you want to.

#### Sample Input 1
```
18
```

#### Sample Output 1
```
1122
1202
1210
2002
2010
10002
10010
```

#### Sample Input 2
```
73
```

#### Sample Output 2
```
112121
112201
120121
120201
121001
200121
200201
201001
1000121
1000201
1001001
```
