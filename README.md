# pacman
PAC-MAN esque game in Python 3
<br />
## functions and files
<br />
pacman.py 
serves as the main, reading the input-file, running the game, and saving to the output-file <br />
gameFunctions.py
contain the main game functions<br /> <br />
input: input-file.txt
specifies board dimensions, starting position, "NESW" moves, and wall positions on the board <br />
output: game-file.txt
saves visualizations of the starting and ending board with walls denoted by nan, 0 the position of pacman, and 1 as any other space <br />
other: test-cases.txt
contains test cases used to build/refine the game

## playing the game
<br />

to play the game, simply run the following command: `python3 pacman.py <input-file.txt>`. the program can accept variable name input files, simply replace `<input-file.txt>` with your filename. <br />

you can edit the input file to the desired game and moves you'd like. for example: <br />

5 5 <br />
1 2 <br />
EEEEE <br />
0 0 <br />
0 1 <br />
0 2 <br />
0 3 <br />
0 4 <br />

this specifies a board of 5x5 dimensions (line 1), starting point of (1,2) (line 2), 5 moves to the right (line 3), and walls all along the left side of the board (lines 4-8). <br /><br />
if any of these inputs are not compatible with the game, an appropriate error message and explanation will appear on the terminal. the edge cases that informed these error messages (and other possible games) can be viewed in the test-cases.txt. <br /><br />
if the inputs are good, the game will run, and the outcome will display on the terminal, with the first line referring to the final position of the pacman and the second line referring to the number of coins you collected! <br /><br />
finally, for visualization, the starting and ending position of the board is saved and displayed on the game-file.txt document. <br />

## hope you have a good game!
