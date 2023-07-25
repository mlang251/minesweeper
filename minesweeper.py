from game import Game

def main():

	difficulty = input('Welcome to Marksweeper! Easy, Medium, or Hard difficulty?\n')
	game = Game(difficulty)

	try:
		while game.in_progress:

			coordinates = ''
			operation = ''
			while True:
				coordinates = input('Enter coordinates: ')
				if coordinates in game.board_layout:
					break
				else:
					print('Enter valid coordinates\n')

			while True:
				operation = input('Flip, Flag, or Question? ')
				if operation.lower() in ['flip', 'flag', 'question']:
					break
				else:
					print('Enter a valid operation\n')
			game.play(coordinates, operation)

	except KeyboardInterrupt:
		print('\nSee you next time!')


if __name__ == "__main__":
	main()
