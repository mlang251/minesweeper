from string import ascii_letters as letters
import random

class Game():

	def __init__(self, difficulty, in_progress = True):
		self.in_progress = in_progress

		# .size is based on difficulty - easy = 8 x 8, medium = 14 x 14, hard = 20 x 20
		# .num_mines is based on difficulty - easy = 10, medium = 40, hard = 80
		if difficulty == 'easy':
			self.size = 8
			self.num_mines = 10
		elif difficulty == 'medium':
			self.size = 14
			self.num_mines = 40
		else:
			self.size = 20
			self.num_mines = 80

		self.generate_minefield()
		self.draw_board()

	def generate_board(self):
		# Create a square array of .size
		# Generate num_mines random unique letter-int pairings, these are the coordinates of the mines - create Tile instances with is_mine = True
		# Iterate through each spot in the square array, if type == Tile, skip it, otherwise create Tile with coordinates (the current iteration in the nested for loop), 
		# 	and num_adjacent_mines (which will requre iterating around all adjacent spaces and counting)


	def draw_board(self):
		# Save this as a last step, get the functional stuff working first
		# Print the game board as it currently is, with flipped tiles, flags, question marks
		pass

	def win(self):
		self.draw_board()
		print('You win!')
		self.in_progress = False

	def lose(self):
		# Reveal all remaining mines
		self.draw_board()
		print('You lose :(')
		self.in_progress = False

class Tile():

	def __init__(self, coordinates, num_adjacent_mines, is_mine = False, is_flipped = False, is_flagged = False, is_question = False):
		self.coordinates = coordinates
		self.num_adjacent_mines = num_adjacent_mines
		self.is_mine = is_mine
		self.is_flipped = is_flipped
		self.is_flagged = is_flagged
		self.is_question = is_question



def main():

	difficulty = input('Welcome to Marksweeper! Easy, Medium, or Hard difficulty?\n')
	game = Game(difficulty)

	try:
		while game.in_progress:
			player_input = input('Choose a tile to flip, flag, or question')

	except KeyboardInterrupt:
		print('See you next time!')



if __name__ == "__main__":
	main()
