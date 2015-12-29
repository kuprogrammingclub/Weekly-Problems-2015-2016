## Intermediate 2 - Space Code Breaking
__Source__: https://www.reddit.com/r/dailyprogrammer/comments/38fjll/20150603_challenge_217_intermediate_space_code/

Copying my ASCII data over as input is causing problems. I see that some people
who were true heroes and tackled the problem early are seeing this. To fix this
we will be altering the challenge. Input will be a set of numbers each represent
a byte in the message. Hopefully this will fix the issues.
<br><br>

#### Input Format

Message broken down into numbers representing the ASCII values of the message between " "

#### Output Format

The name of the system and the message decoded.
<br><br>

#### Encryption & Planet Systems
```
Omicron V: will take and invert the 5th bit. (0001 0000) That is the bit location
in the byte where we invert the bit.

Hoth: Takes the value of the ASCII character and adds 10 to it.

Ryza IV: Takes the value of the ASCII character and subtracts 1 to it.

Htrae: reverses the characters.
```
<br>

#### Validation

It is not enough to just take the message and decode it in all 4 ways and let
you decide which one is right or wrong. You need to have your program/solution
determine the right decoding. All messages are in english (I know even in the
future on alien planets).

<br>

#### Sample Input
```
" 101 99 97 101 112 32 110 105 32 101 109 111 99 32 101 87 "
```

#### Sample Output
```
Htrae: We come in Peace
```
