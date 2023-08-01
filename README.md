# minesweeper
This is Marksweeper, my version of Minesweeper built as a terminal game. I built this for a portfolio project as part of the Codecademy Computer Science professional certification course. The project gave me great hands on experience with object oriented programming, handling user input, checking edge cases, and I even got to use some recursion! Very fun.

It's so much fun to win! What's going on in this gif? User inputs a row, column and operation (flip, flag, or question) for each turn. After each turn the board is redrawn and each tile object represents itself based on a few attributes. You can also see the recursion in action here when flipping a tile which has 0 adjacent mines. Notice how many adjacent Tiles are immediately flipped!

![](https://github.com/mlang251/minesweeper/blob/main/gifs/you-win.gif)



And it's still a litle bit fun to lose. If you flip a tile that is a mine, the remaining mines will be revealed and it's game over.

![](https://github.com/mlang251/minesweeper/blob/main/gifs/you-lose.gif)
