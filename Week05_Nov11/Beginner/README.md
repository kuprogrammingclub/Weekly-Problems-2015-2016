## Beginner - Evaluating e<sup>x</sup>
__Source__: https://www.hackerrank.com/challenges/eval-ex

The series expansion of ex is given by:

1 + x + x<sup>2</sup>/2! + x<sup>3</sup>/3! + x<sup>4</sup>/4! + .......

Evaluate e^x for given values of x, by using the above expansion for the first 10
terms. The challenge is to accomplish this without either mutable state, or direct
declaration of local variables.

#### Input Format

The first line contains an integer number N which will be the number of test cases.
N lines follow, each line containing a value of x for which you need to output the
value of e<sup>x</sup> using the above series expansion.These input values have
exactly 4 decimal places each.

#### Output Format

N lines, each of them containing the value of e<sup>x</sup>, computed by your program.

#### Sample Input
```
4
20.0000
5.0000
0.5000
-0.5000
```

#### Sample Output
```
2423600.1887
143.6895
1.6487
0.6065
```
