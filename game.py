from tile import Tile
import random

class Game:
	def __init__(self, difficulty, in_progress = True):
		self.in_progress = in_progress

		# .size is based on difficulty - easy = 8 x 8, medium = 14 x 14, hard = 20 x 20
		# .num_mines is based on difficulty - easy = 10, medium = 40, hard = 80
		difficulty = difficulty.lower()
		if difficulty == 'easy':
			self.size = 8
			self.num_mines = 10
		elif difficulty == 'medium':
			self.size = 14
			self.num_mines = 40
		else:
			self.size = 20
			self.num_mines = 80

		self.generate_board()
		self.draw_board()

	def generate_board(self):

		# Create a square array of .size
		self.board_layout = [[' ' for j in range(self.size)] for i in range(self.size)]

		# Generate a list of integers which represents the indices of mines when iterating through all spaces in the board
		# Then create a Tile object in each space, with is_mine set to True if the counter is in the mine_indices list
		mine_indices = random.sample(list(range(self.size ** 2)), self.num_mines)
		counter = 0
		for row in range(self.size):
			for column in range(self.size):
				self.board_layout[row][column] = Tile((row, column), is_mine=counter in mine_indices)
				counter += 1

		# Iterate through all Tiles and set .num_adjacent_mines for each
		for row in range(self.size):
			for column in range(self.size):
				tile = self.get_tile(row, column)
				if not tile.is_mine:
					adjacent_tiles = self.get_adjacent_tiles(tile)
					num_adjacent_mines = 0
					for coordinates in adjacent_tiles:
						adjacent_row, adjacent_column = coordinates
						# We are only concerned with coordinates that are actually on the board
						if 0 <= adjacent_row < self.size and 0 <= adjacent_column < self.size:
							adjacent_tile = self.get_tile(adjacent_row, adjacent_column)
							if adjacent_tile.is_mine:
								num_adjacent_mines += 1
					tile.num_adjacent_mines = num_adjacent_mines

	def get_tile(self, row, column):
		return self.board_layout[row][column]

	def flip_tile(self, tile):
		tile.is_flipped = True
		if tile.is_mine:
			# TODO - should probably call .lose() from .play()
			self.lose()
			return None
		else:
			# TODO - Fix this, RecursionError: maximum recursion depth exceeded
			adjacent_mines = tile.num_adjacent_mines
			if adjacent_mines < 0:
				print('Error! tile has negative number of adjacent mines')
				return None
			elif adjacent_mines > 0:
				return adjacent_mines
			else:
				adjacent_tiles = self.get_adjacent_tiles(tile)
				for coordinates in adjacent_tiles:
					row, column = coordinates
					this_tile = self.get_tile(row, column)
					self.flip_tile(this_tile)

	def play(self, row, column, operation):
		tile = self.get_tile(row, column)
		if tile.is_flipped:
			print('Tile {coordinates} is already flipped'.format(coordinates=(row, column)))
			return

		if operation.lower() == 'flag':
			tile.toggle_flag()
		elif operation.lower() == 'question':
			tile.toggle_question()
		else:
			self.flip_tile(tile)

		print('row {row}, column {column}: {operation}'.format(row=row, column=column, operation=operation))
		self.draw_board()

	def get_adjacent_tiles(self, tile):
		row, column = tile.coordinates
		# Return coordinates of all adjacent tiles (note, if a tile is on the edge, some of these will be out of bounds)
		# TODO - only return valid tile coordinates, remove any unnecessary error handling at locations that call this method
		return [(row-1, column-1), (row-1, column), (row-1, column+1),
				(row, column-1), (row, column+1),
				(row+1, column-1), (row+1, column), (row+1, column+1)]

	def draw_board(self):
		# Save this as a last step, get the functional stuff working first
		# Print a visual representation of the game board as it currently is, with flipped tiles, flags, question marks
		for i in range(self.size):
			row = ''
			for j in range(self.size):
				row += '[{}]'.format(self.board_layout[i][j])
			print(row)

	def win(self):
		self.draw_board()
		print('You win!')
		self.in_progress = False

	def lose(self):
		# Reveal all remaining mines
		self.draw_board()
		print('You lose :(')
		self.in_progress = False