## Beginner 1 - Funny String
__*Source*__: https://www.hackerrank.com/challenges/funny-string

Suppose you have a string S which has length N and is indexed from 0 to N−1.
String R is the reverse of the string S. The string S is funny if the condition
<br><br>
|S<sub>i</sub> − S<sub>i − 1</sub>| = |R<sub>i</sub> − R<sub>i − 1</sub>|
<br><br>
is true for every i from 1 to N − 1.

(Note: Given a string str, str<sub>i</sub> denotes the ascii value of the i<sup>th</sup> character (0-indexed) of str. |x| denotes the absolute value of an integer x)

For each string, print Funny or Not Funny in separate lines.
Also, assume we're only using lowercase due to the fact that mixing case would
involve odd offsets.

#### Sample Input
```
acxz
bcxz
```

#### Sample Output
```
Funny
Not Funny
``` 
