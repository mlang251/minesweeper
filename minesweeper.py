from game import Game


def main():

	difficulty = ''
	while True:
		user_input = input('Welcome to Marksweeper! Easy, Medium, or Hard difficulty?\n')
		if user_input.lower() in ['easy', 'medium', 'hard']:
			difficulty = user_input.lower()
			break
	game = Game(difficulty)

	try:
		while game.in_progress:
			row = ''
			column = ''
			operation = ''
			while True:
				try:
					# Subtracting 1 from row because board is represented as 1-indexed, but we want 0 indexed input
					row = int(input('Enter row: ')) - 1
				except ValueError:
					print('Enter valid row number')
				else:
					# Check row is in the bounds of the game board
					if 0 <= row < game.size:
						break
					else:
						print('Enter valid row number')

			while True:
				try:
					# Subtracting 1 from column because board is represented as 1-indexed, but we want 0 indexed input
					column = int(input('Enter column: ')) - 1
				except ValueError:
					print('Enter valid column number')
				else:
					# Check column is in the bounds of the game board
					if 0 <= column < game.size:
						break
					else:
						print('Enter valid column number')

			while True:
				operation = input('Flip, Flag, or Question? ')
				if operation.lower() in ['flip', 'flag', 'question']:
					break
				else:
					print('Enter a valid operation')
			game.play(row, column, operation)

	except KeyboardInterrupt:
		print('\nSee you next time!')


if __name__ == "__main__":
	main()
