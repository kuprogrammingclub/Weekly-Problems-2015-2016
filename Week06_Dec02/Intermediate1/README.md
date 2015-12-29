## Intermediate 1 - VHS Recording Problem
__Source__: https://www.reddit.com/r/dailyprogrammer/comments/3u6o56/20151118_challenge_242_intermediate_vhs_recording/

All nineties kids will remember the problem of having to program their VHS
recorder to tape all their favorite shows. Especially when 2 shows are aired at
the same time, which show do we record? Today we are going to program the recorder,
so that we have a maximum amount of tv shows on one tape.<br>

You receive a timetable with when the shows start and when it ends. All times
are in Military time. We can switch between channels instantaneously, so if a
shows start on the same time a other one stops, you can record them.<br>


### Part 1
We want to know what shows we have recorded, so instead of showing the number of
shows, show the names of the shows we recorded.

#### Sample Input 1
```
1535 1610 Pokémon
1610 1705 Law & Order
1615 1635 ER
1615 1635 Ellen
1615 1705 Family Matters
1725 1810 The Fresh Prince of Bel-Air
```

#### Sample Output 1
```
Pokémon
Law & Order
The Fresh Prince of Bel-Air
```

### Part 2

Now the first line will be a must see show. We don't care if we don't max out
the number of shows, but we sure want to have our favorite recorded.

#### Sample Input 2
```
The Fresh Prince of Bel-Air
1530 1555 3rd Rock from the Sun
1550 1615 The Fresh Prince of Bel-Air
1555 1615 Mad About You
1615 1650 Ellen
1655 1735 Quantum Leap
```

#### Sample Output 2
```
The Fresh Prince of Bel-Air
Ellen
Quantum Leap
```
