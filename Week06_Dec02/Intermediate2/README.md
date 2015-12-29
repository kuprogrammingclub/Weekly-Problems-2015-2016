## Intermediate 2 - Quicksort In-Place
__Source__: https://www.hackerrank.com/challenges/quicksort3

Create an in-place version of Quicksort. You need to follow
[Lomuto Partitioning](http://en.wikipedia.org/wiki/Quicksort#Algorithm) method.

#### Input Description
There will be two lines of input:<br>
n - the size of the array<br>
ar - the n numbers of the array<br>

#### Output Format
Print the entire array on a new line at the end of every partitioning method.

#### Constraints
1 ≤ n ≤ 5000<br>
−10000 ≤ x ≤ 10000, x ∈ ar<br>
There are no duplicate numbers.<br>

#### Sample Input
```
7
1 3 9 8 2 7 5
```

#### Sample Output
```
1 3 2 5 9 7 8
1 2 3 5 9 7 8
1 2 3 5 7 8 9
```
