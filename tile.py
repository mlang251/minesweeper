class Tile:

	def __init__(self, coordinates, is_mine = False, num_adjacent_mines = None, is_flipped = False, is_flagged = False, is_question = False):
		self.coordinates = coordinates					# tuple of zero indexed row, column pairs
		self.is_mine = is_mine
		self.num_adjacent_mines = num_adjacent_mines
		self.is_flipped = is_flipped
		self.is_flagged = is_flagged
		self.is_question = is_question

	def __repr__(self):
		if self.is_flipped:
			return 'X' if self.is_mine else str(self.num_adjacent_mines)
		elif self.is_flagged:
			return 'F'
		elif self.is_question:
			return '?'
		else:
			return ' '

	def toggle_flag(self):
		if self.is_question:
			self.toggle_question()
		self.is_flagged = not self.is_flagged

	def toggle_question(self):
		if self.is_flagged:
			self.toggle_flag()
		self.is_question = not self.is_question