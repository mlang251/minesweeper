class Tile():

	def __init__(self, coordinates, num_adjacent_mines = 0, is_mine = False, is_flipped = False, is_flagged = False, is_question = False):
		self.coordinates = coordinates
		self.num_adjacent_mines = num_adjacent_mines
		self.is_mine = is_mine
		self.is_flipped = is_flipped
		self.is_flagged = is_flagged
		self.is_question = is_question

	def __repr__(self):
		return str(self.is_mine)