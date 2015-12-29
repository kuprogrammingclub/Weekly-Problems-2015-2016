## Intermediate 2 - The Grid Search
__*Source*__: https://www.hackerrank.com/challenges/the-grid-search

Given a 2D array of digits, try to find the location of a given 2D pattern of digits. For example, consider the following 2D matrix:

```
1234567890  
0987654321  
1111111111  
1111111111  
2222222222  
```

Assume we need to look for the following 2D pattern:

```
876543  
111111  
111111
```

If we scan through the original array, we observe that the 2D pattern begins at the second row and the third column of the larger grid (the 8 in the second row and third column of the larger grid is the top-left corner of the pattern we are searching for).

So, a 2D pattern of P digits is said to be present in a larger grid G, if the latter contains a contiguous, rectangular 2D grid of digits matching with the pattern P, similar to the example shown above.

Display 'YES' or 'NO', depending on whether (or not) you find that the larger grid G contains the rectangular pattern P. The evaluation will be case sensitive.

#### Sample Input
```
2
10 10
7283455864
6731158619
8988242643
3830589324
2229505813
5633845374
6473530293
7053106601
0834282956
4607924137
3 4
9505
3845
3530
15 15
400453592126560
114213133098692
474386082879648
522356951189169
887109450487496
252802633388782
502771484966748
075975207693780
511799789562806
404007454272504
549043809916080
962410809534811
445893523733475
768705303214174
650629270887160
2 2
99
99
```

#### Sample Output
```
YES
NO
```

__NOTE:__ HackerRank has a more detailed explanation at the source URL, so if
you don't understand this small snippet of the problem statement, make sure to
read the full one.
