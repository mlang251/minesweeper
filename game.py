from tile import Tile
import random


class Game:
    def __init__(self, difficulty, in_progress=True):
        self.in_progress = in_progress
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

        self.num_safe_tiles_remaining = self.size ** 2 - self.num_mines
        self.board_layout = [[None for i in range(self.size)] for j in range(self.size)]

        self.generate_board()
        self.draw_board()

    def get_tile(self, row, column):
        return self.board_layout[row][column]

    def get_adjacent_tiles(self, tile):
        # Note - if a tile is on the edge of the board some of these will be out of bounds
        row, column = tile.get_coordinates()
        return [(row - 1, column - 1), (row - 1, column), (row - 1, column + 1),
                (row, column - 1), (row, column + 1),
                (row + 1, column - 1), (row + 1, column), (row + 1, column + 1)]

    def set_num_adjacent_mines(self, tile):
        adjacent_tiles = self.get_adjacent_tiles(tile)
        num_adjacent_mines = 0
        for coordinates in adjacent_tiles:
            adjacent_row, adjacent_column = coordinates
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
        column_numbers = []
        for i in range(self.size):
            # Printing these numbers gets funky when going to double digits, so a variable padding is needed
            padding = " " if i + 1 < 10 else ""
            column_number = str(i + 1)
            column_numbers.append(f"{padding}{column_number} ")
        print("  " + "".join(column_numbers))
        for i in range(self.size):
            padding = " " if i + 1 < 10 else ""
            row = str(i + 1) + padding
            for j in range(self.size):
                tile = self.board_layout[i][j]
                row += f"[{tile}]"
            print(row)

    def flip_tile(self, tile):
        tile.is_flipped = True
        if tile.is_mine:
            return "mine"
        else:
            self.num_safe_tiles_remaining -= 1
            adjacent_mines = tile.num_adjacent_mines
            if adjacent_mines < 0:
                print("Error! tile has negative number of adjacent mines")
                return None
            elif adjacent_mines > 0:
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
            if 0 <= row < self.size and 0 <= column < self.size:
                adjacent_tile = self.get_tile(row, column)
                if not adjacent_tile.is_flipped:
                    self.flip_tile(adjacent_tile)

    def play(self, row, column, operation):
        tile = self.get_tile(row, column)
        if tile.is_flipped:
            print("Tile {coordinates} is already flipped".format(coordinates=(row + 1, column + 1)))
            return

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
        print("\n")
        self.draw_board()

    def win(self):
        print("\n")
        self.draw_board()
        print("You win!\n")
        self.in_progress = False

    def lose(self):
        for row in self.board_layout:
            for tile in row:
                if tile.is_mine and not tile.is_flipped:
                    self.flip_tile(tile)
        print("\n")
        self.draw_board()
        print("You lose :(\n")
        self.in_progress = False
