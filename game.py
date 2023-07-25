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
		letters = ascii_letters[:self.size]
		numbers = list(range(1, self.size + 1))

		self.board_layout = []
		for letter in letters:
			for number in numbers:
				self.board_layout.append(letter + str(number))

		# Generate num_mines random unique letter-int pairings, these are the coordinates of the mines - create Tile instances with is_mine = True
		mine_locations = random.sample(self.board_layout, self.num_mines)

		# Iterate through each spot in the square array, if type == Tile, skip it, otherwise create Tile with coordinates (the current iteration in the nested for loop), 
		# 	and num_adjacent_mines (which will requre iterating around all adjacent spaces and counting)
		self.tiles = {}
		for space in self.board_layout:
			self.tiles[space] = Tile(space, is_mine = space in mine_locations)

	def play(self, coordinates, operation):
		print(coordinates + ': ' + operation)

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