from tile import Tile
import random


class Game:
    def __init__(self, difficulty, in_progress=True):
        self.in_progress = in_progress

        # .size is based on difficulty - easy = 8 x 8, medium = 14 x 14, hard = 20 x 20
        # .num_mines is based on difficulty - easy = 10, medium = 40, hard = 80
        difficulty = difficulty.lower()
        if difficulty == "easy":
            self.size = 8
            self.num_mines = 10
        elif difficulty == "medium":
            self.size = 14
            self.num_mines = 40
        else:
            self.size = 20
            self.num_mines = 80

        # Create a square array of .size
        self.board_layout = [[None for i in range(self.size)] for j in range(self.size)]
        # This attribute is needed to determine the win condition
        self.num_safe_tiles_remaining = self.size**2 - self.num_mines

        self.generate_board()
        self.draw_board()

    def get_tile(self, row, column):
        return self.board_layout[row][column]

    def get_adjacent_tiles(self, tile):
        row, column = tile.coordinates
        # Return coordinates of all adjacent tiles (note, if a tile is on the edge, some of these will be out of bounds)
        return [(row - 1, column - 1), (row - 1, column), (row - 1, column + 1),
                (row, column - 1), (row, column + 1),
                (row + 1, column - 1), (row + 1, column), (row + 1, column + 1)]

    def set_num_adjacent_mines(self, tile):
        adjacent_tiles = self.get_adjacent_tiles(tile)
        num_adjacent_mines = 0
        for coordinates in adjacent_tiles:
            adjacent_row, adjacent_column = coordinates
            # Coordinates from get_adjacent_tiles might be out of bounds
            # so check to see if the coordinates are a valid Tile
            if 0 <= adjacent_row < self.size and 0 <= adjacent_column < self.size:
                adjacent_tile = self.get_tile(adjacent_row, adjacent_column)
                if adjacent_tile.is_mine:
                    num_adjacent_mines += 1
        tile.num_adjacent_mines = num_adjacent_mines

    def generate_board(self):
        # Generate a list of integers which represents the indices of mines when iterating through all spaces in the board
        # Then create a Tile object in each space, with is_mine set to True if the counter is in the mine_indices list
        mine_indices = random.sample(list(range(self.size**2)), self.num_mines)
        counter = 0
        for row in range(self.size):
            for column in range(self.size):
                self.board_layout[row][column] = Tile((row, column), is_mine=(counter in mine_indices))
                counter += 1

        # Iterate through all Tiles and set .num_adjacent_mines for each
        for row in range(self.size):
            for column in range(self.size):
                tile = self.get_tile(row, column)
                if not tile.is_mine:
                    self.set_num_adjacent_mines(tile)

    def draw_board(self):
        # Print a visual representation of the game board as it currently is, with flipped tiles, flags, question marks
        # First print the header row with 1-indexed column numbers
        column_numbers = []
        for i in range(self.size):
            # Printing these numbers gets funky when going to double digits, so a variable padding is needed
            padding = " " if i + 1 < 10 else ""
            column_number = str(i + 1)
            column_numbers.append(f"{padding}{column_number} ")
        print("  " + "".join(column_numbers))

        # Now print each row number followed by the Tiles in that row. Tile class has a .__repr__ method, so each
        # Tile can display whatever information is relevant
        for i in range(self.size):
            padding = " " if i + 1 < 10 else ""
            row = str(i + 1) + padding
            for j in range(self.size):
                tile = self.board_layout[i][j]
                row += f"[{tile}]"
            print(row)

    def flip_tile(self, tile):
        # Flip a tile and check if it's a mine. If it's a mine, game is over
        tile.is_flipped = True
        if tile.is_mine:
            return "mine"
        else:
            # If it's a safe space, we need to check how many adjacent mines there are
            self.num_safe_tiles_remaining -= 1
            adjacent_mines = tile.num_adjacent_mines
            if adjacent_mines < 0:
                print("Error! tile has negative number of adjacent mines")
                return None
            elif adjacent_mines > 0:
                # If there are adjacent mines, we can exit the .flip_tile method. The tile will now be represented
                # 	by the number of adjacent mines when the board is printed
                return None
            else:
                # If there are no adjacent mines, we need to flip all adjacent tiles recursively until tiles with
                # 	adjacent mines are discovered
                self.flip_adjacent_tiles(tile)
                return None

    def flip_adjacent_tiles(self, tile):
        adjacent_tiles = self.get_adjacent_tiles(tile)
        for coordinates in adjacent_tiles:
            row, column = coordinates
            # if the coordinates are a valid Tile that has not been flipped, flip that Tile
            if 0 <= row < self.size and 0 <= column < self.size:
                adjacent_tile = self.get_tile(row, column)
                if not adjacent_tile.is_flipped:
                    self.flip_tile(adjacent_tile)

    def play(self, row, column, operation):
        # row, column, and operation were user inputs for an operation to perform on a certain Tail
        tile = self.get_tile(row, column)
        if tile.is_flipped:
            # If the Tile is already flipped, there's nothing we can do this turn
            print("Tile {coordinates} is already flipped".format(coordinates=(row + 1, column + 1)))
            return

        # Flag, Question, or Flip the Tile and then draw the board again
        if operation.lower() == "flag":
            tile.toggle_flag()
        elif operation.lower() == "question":
            tile.toggle_question()
        else:
            # Result of .flip_tile is only used to tell if the user flipped a mine. Otherwise a return value is not needed
            result = self.flip_tile(tile)
            if result == "mine":
                self.lose()
                return
            elif self.num_safe_tiles_remaining == 0:
                self.win()
                return
        # After all the logic is done for this turn, draw a current representation of the game board
        print("\n")
        self.draw_board()

    def win(self):
        # All safe spaces have been flipped!
        print("\n")
        self.draw_board()
        print("You win!\n")
        self.in_progress = False

    def lose(self):
        # Flip all remaining mines
        for row in self.board_layout:
            for tile in row:
                if tile.is_mine and not tile.is_flipped:
                    self.flip_tile(tile)
        print("\n")
        self.draw_board()
        print("You lose :(\n")
        self.in_progress = False
