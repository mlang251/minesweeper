class Tile:

	def __init__(self, coordinates, is_mine = False, num_adjacent_mines = None, is_flipped = False, is_flagged = False, is_question = False):
		self.coordinates = coordinates					# tuple of zero indexed row, column pairs
		self.is_mine = is_mine
		self.num_adjacent_mines = num_adjacent_mines
		self.is_flipped = is_flipped
		self.is_flagged = is_flagged
		self.is_question = is_question

	def __repr__(self):
		# TODO - these representations need to be fixed. If a tile is a mine it takes precedence over flag or question
		# 	if the lose condition is hit. Also if user questions a flag, it shoud change to a question, and vice versa
		# 	this logic should be in the toggle_ methods
		if self.is_flagged:
			return 'F'
		elif self.is_question:
			return '?'
		elif self.is_flipped:
			return 'X' if self.is_mine else str(self.num_adjacent_mines)
		else:
			return ' '

	def toggle_flag(self):
		self.is_flagged = not self.is_flagged

	def toggle_question(self):
		self.is_question = not self.is_question