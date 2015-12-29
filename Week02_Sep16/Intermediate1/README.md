## Intermediate 1 - Parentheses Matching
__*Source*__: https://www.hackerrank.com/challenges/java-stack

A string containing only parentheses is balanced if the following is true:
1. if it is an empty string
2. if A and B are correct, AB is correct,
3. if A is correct, (A) and {A} and [A] are also correct.

Examples of some correctly balanced strings are: "{}()", "[{()}]", "({()})"<br>
Examples of some unbalanced strings are: "{}(", "({)}", "[[", "}{" etc.

Given a string, determine if it is balanced or not.
For each case, print 'true' if the string is balanced, 'false' otherwise.

#### Sample Input
```
{}()
({()})
{}(
[]
```

#### Sample Output
```
true
true
false
true
```
