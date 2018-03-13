# Sudoku
Free time project that solves Sudoku that I did during Python course.



### Example for input - 

```
{
  1:{2:7,3:5,5:2,6:3,7:8},
  2:{2:9,5:8,9:3},
  3:{3:6,5:4,9:1},
  4:{1:5,5:4},
  5:{1:7,3:2,4:8,6:6,7:9,9:1},
  6:{5:2,9:3},
  7:{1:9,5:6,7:7},
  8:{1:4,5:7,8:1},
  9:{3:7,4:5,5:8,7:3,8:9}
}
```
The outer dictionary is the board dictionary and it splits the board to the 9 big squares.
The inner dictionaries are dictionaries that split each square into the 9 small squares that contain the numbers (ordered left to right).

The board from the example above would look like this:
```
_________________________________
|    7  5 ||    9    ||       6 ||
|    2  3 ||    8    ||    4    ||
| 8       ||       3 ||       1 ||
_________________________________
| 5       || 7     2 ||         ||
|    4    || 8     6 ||    2    ||
|         || 9     1 ||       3 ||
_________________________________
| 9       || 4       ||       7 ||
|    6    ||    7    || 5  8    ||
| 7       ||    1    || 3  9    ||
_________________________________
```
