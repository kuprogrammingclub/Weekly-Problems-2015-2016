## Intermediate 1 - Sherlock & Watson
__Source__: https://www.hackerrank.com/challenges/sherlock-and-watson

John Watson performs an operation called Right Circular Rotation on an integer
array [a<sub>0</sub>, a<sub>1</sub>,..., a<sub>N−1</sub>]. Right Circular Rotation
transforms the array from [a<sub>0</sub>, a<sub>1</sub>, ..., a<sub>N−1</sub>] to
[a<sub>N−1</sub>, a<sub>0</sub>, ..., a<sub>N−2</sub>].

He performs the operation *K* times and tests Sherlock's ability to identify
the element at a particular position in the array. He asks *Q* queries. Each
query consists of one integer, *idx*, for which you have to print the element
at index idx in the rotated array, i.e. <i>a</i><sub><i>idx</i></sub>.

#### Input Format

The first line consists of three integers, *N*, *K*, and *Q*, separated by a single space.
The next line contains *N* space-separated integers which indicate the elements of the array *A*.<br>
Each of the next *Q* lines contains one integer per line denoting *idx*.

#### Output Format

For each query, print the value at index *idx* in the updated array separated by
newline.

#### Sample Input
```
3 2 3
1 2 3
0
1
2
```

#### Sample Output
```
2
3
1
```
