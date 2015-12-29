## Intermediate 2 - Fallout Hacking Game
__Source__: https://www.reddit.com/r/dailyprogrammer/comments/3qjnil/20151028_challenge_238_intermediate_fallout/


The popular video games Fallout 3 and Fallout: New Vegas have a computer "hacking"
mini-game where the player must correctly guess the correct password from a list of
same-length words. Your challenge is to implement this game yourself.<br>
The game operates similarly to the classic board game Mastermind. The player has
only 4 guesses and on each incorrect guess the computer will indicate how many
letter positions are correct.<br>
For example, if the password is MIND and the player guesses MEND, the game will
indicate that 3 out of 4 positions are correct (M_ND). If the password is COMPUTE
and the player guesses PLAYFUL, the game will report 0/7. While some of the letters
match, they're in the wrong position.<br>
Ask the player for a difficulty (very easy, easy, average, hard, very hard),
then present the player with 5 to 15 words of the same length. The length can
be 4 to 15 letters. More words and letters make for a harder puzzle. The player
then has 4 guesses, and on each incorrect guess indicate the number of correct
positions.

#### Example
```
Difficulty (1-5)? 3
SCORPION
FLOGGING
CROPPERS
MIGRAINE
FOOTNOTE
REFINERY
VAULTING
VICARAGE
PROTRACT
DESCENTS
Guess (4 left)? migraine
0/8 correct
Guess (3 left)? protract
2/8 correct
Guess (2 left)? croppers
8/8 correct
You win!
```

You can draw words from this dictionary file:
[enable1.txt](http://code.google.com/p/dotnetperls-controls/downloads/detail?name=enable1.txt).
Your program should completely ignore case when making the position checks.<br>
There may be ways to increase the difficulty of the game, perhaps even making it
impossible to guarantee a solution, based on your particular selection of words.
For example, your program could supply words that have little letter position
overlap so that guesses reveal as little information to the player as possible.
