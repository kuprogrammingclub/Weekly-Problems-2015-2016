## Intermediate 1 - Scoring a Bowling Game
__Source__: https://www.reddit.com/r/dailyprogrammer/comments/3ntsni/20151007_challenge_235_intermediate_scoring_a/


You'll be given a bowling sheet for a single person on a line, with the ten frames
separated by a space. All scores are single characters: - for zero (aka a gutter
ball), 1-9 for 1-9 pins knocked down, / for a spare, and X for a strike. If you
see any two digit numbers (e.g. "63") that's actually the first and second ball
scores (a six then a three). Example:

```
X X X X X X X X X XXX
```

Your program should calculate the score for the sheet and report it. From our example:

```
300
```

Aka a perfect game.

#### Challenge Input
```
X -/ X 5- 8/ 9- X 81 1- 4/X
62 71  X 9- 8/  X  X 35 72 5/8
```

#### Challenge Output
```
137
140
```
