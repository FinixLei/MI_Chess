# MI_Chess
This is to solve a game called MI chess.

```
R-R-R
|\|/|
E-E-E
|/|\|
B-B-B
```

'R' means red stone, 'E' means empty, 'B' means black stone.

## Rules to play
There are 3 red stones and 3 black stones on the board.  
Red player can move one red stone by one step along the row, column or slash for one time.  
The same for the black player.  
Start from Red player.  
If one player has no available moves, it can pass; otherwise, it cannot pass.   
Who puts its own 3 stones in the same line, i.e. row, column or slash, will win.  
Note, if put the 3 stones to its own initial position, it does not count as a win.  

## How to play with the AI
Show the example as below.

```
python .\Game.py
Please choose RED or BLACK (R or B):
R
R1-R2- R3
| \ | / |
4 - 5-  6
| / | \ |
B1-B2- B3
------------------------------
Please enter your move (e.g. R1->4):
R2->5
R1- 2- R3
| \ | / |
4 -R2-  6
| / | \ |
B1-B2- B3
------------------------------
Engine Move: B3->6
R1- 2- R3
| \ | / |
4 -R2- B3
| / | \ |
B1-B2-  9
------------------------------
Please enter your move (e.g. R1->4):
R2->9
R1- 2- R3
| \ | / |
4 - 5- B3
| / | \ |
B1-B2- R2
------------------------------
Engine Move: B1->5
R1- 2- R3
| \ | / |
4 -B1- B3
| / | \ |
7 -B2- R2
------------------------------
Please enter your move (e.g. R1->4):
R1->4
1 - 2- R3
| \ | / |
R1-B1- B3
| / | \ |
7 -B2- R2
------------------------------
Engine Move: B2->7
1 - 2- R3
| \ | / |
R1-B1- B3
| / | \ |
B2- 8- R2
------------------------------
Please enter your move (e.g. R1->4):
R3->2
1 -R3-  3
| \ | / |
R1-B1- B3
| / | \ |
B2- 8- R2
------------------------------
Engine Move: B3->3
1 -R3- B3
| \ | / |
R1-B1-  6
| / | \ |
B2- 8- R2
------------------------------
Black Win!
```

(END)
