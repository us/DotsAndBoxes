import board

import player

Board = board.Board()

PlayerA = player.Player()

PlayerB = player.Player()


def play_game():
	playerA_score = PlayerA.score
	playerB_score = PlayerB.score
	Board.print_board()
	if Board.end_game():
		print("Player "+Board.current_player.initial+" Wins!")
		if playerA_score > playerB_score:
			PlayerA.num_wins += 1
		else:
			PlayerB.num_wins += 1
		return
	elif Board.tie():
		print("It's a Tie!")
		return
	enter_coordinates()
	if Board.current_player == PlayerA:
		if playerA_score == PlayerA.score:
			Board.current_player = PlayerB
			Board.other_player = PlayerA
	elif Board.current_player == PlayerB:
		if playerB_score == PlayerB.score:
			Board.current_player = PlayerA
			Board.other_player = PlayerB
	play_game()

def valid_coordinate(coordinate):
	return (len(coordinate) == 2 and 
		   coordinate[0] in ["0","1","2","3","4","5","6","7","8","9"][:Board.width+1] and
		   coordinate[1] in ["0","1","2","3","4","5","6","7","8","9"][:Board.height+1])

def enter_coordinates():
	print("Player "+Board.current_player.initial+"'s Turn")

	if not Board.current_player.human:
		isPlayerA = (Board.current_player == PlayerA)
		move = Board.alphabeta_search(isPlayerA,PlayerA.score,PlayerB.score)
		print(move)
		Board.set_line(move[:2],move[2:])
		return

	print("Draw a line between adjacent dots by entering the dot coordinates")
	coordinates = raw_input("Enter the Coordinates (in the form xy x'y'): ")
	if coordinates.upper() == "Q" or coordinates.upper() == "QUIT":
		print("Goodbye!")
		quit()
	
	if len(coordinates) == 4:
		if valid_coordinate(coordinates[:2]):
			first = coordinates[:2]
			if valid_coordinate(coordinates[2:]):
				second = coordinates[2:]
				if not Board.set_line(first,second):
					print("Please Enter an Adjacent Set of Coordinates")
					enter_coordinates()
			else:
				print("Please Enter a Valid Set of Coordinates")
				enter_coordinates()
		else:
			print("Please Enter a Valid Set of Coordinates")
			enter_coordinates()

	elif len(coordinates) == 5:
		split = coordinates.split()
		if not coordinates[2] == " ":
			print("Please Enter a Valid Set of Coordinates")
			enter_coordinates()
		elif valid_coordinate(split[0]):
			first = split[0]
			if valid_coordinate(split[1]):
				second = split[1]
				if not Board.set_line(first,second):
					print("Please Enter an Adjacent Set of Coordinates")
					enter_coordinates()
			else:
				print("Please Enter a Valid Set of Coordinates")
				enter_coordinates()
		else:
			print("Please Enter a Valid Set of Coordinates")
			enter_coordinates()
	else:
		print("Please Enter a Valid Set of Coordinates")
		enter_coordinates()

	

def main():
	Board.board_setup()
	print("Please select a one letter name for player 1")
	PlayerA.player_setup(" ")
	print("Please select a different one letter name for player 2")
	PlayerB.player_setup(PlayerA.initial)
	Board.current_player = PlayerA
	Board.other_player = PlayerB
	play_game()
	
if __name__ == "__main__":
    main()