from tile import Tile
from string import ascii_letters
import random

class Game():
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
		# TODO create array of arrays instead
		self.letters = ascii_letters[:self.size]
		self.numbers = list(range(1, self.size + 1))

		self.board_layout = []
		for letter in letters:
			for number in numbers:
				self.board_layout.append(letter + str(number))

		# Generate num_mines random unique letter-int pairings, these are the coordinates of the mines
		mine_locations = random.sample(self.board_layout, self.num_mines)

		# Iterate through each spot in the square array, create a Tile object with the coordinates, and set is_mine = True
		# if the coordinates appear in mine_locations
		# num_adjacent_mines (which will requre iterating around all adjacent spaces and counting)
		self.tiles = {}
		for space in self.board_layout:
			self.tiles[space] = Tile(space, is_mine = space in mine_locations)

	def play(self, coordinates, operation):
		tile = self.tiles[coordinates]
		if operation.lower() == 'flag':
			tile.is_flagged = not tile.is_flagged
		elif operation.lower() == 'question':
			tile.is_question = not tile.is_question
		else:
			tile.is_flipped = True
			if tile.is_mine:
				self.lose()
			else:
				# TODO calculate number of adjacent mines,
				# 	if there are adjacent mines, return this number
				# 	if there are no adjacent mines, recursively flip adjacent tiles in all directions until adjacent mines are found
				pass

		print(coordinates + ': ' + operation)

	def get_adjacent_tiles(self, tile):
		tile_row = tile.coordinates[0]
		tile_column = tile.coordinates[1]
		tile_row_index =

	def draw_board(self):
		# Save this as a last step, get the functional stuff working first
		# Print a visual representation of the game board as it currently is, with flipped tiles, flags, question marks
		print(self.board_layout)

	def win(self):
		self.draw_board()
		print('You win!')
		self.in_progress = False

	def lose(self):
		# Reveal all remaining mines
		self.draw_board()
		print('You lose :(')
		self.in_progress = False