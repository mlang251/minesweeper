from game import Game

def main():

	difficulty = input('Welcome to Marksweeper! Easy, Medium, or Hard difficulty?\n')
	game = Game(difficulty)

	try:
		while game.in_progress:
			row = ''
			column = ''
			operation = ''
			while True:
				row = int(input('Enter row: '))
				if 0 <= row < game.size:
					break
				else:
					print('Enter valid row number')

			while True:
				column = int(input('Enter column: '))
				if 0 <= column < game.size:
					break
				else:
					print('Enter valid row number')

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
