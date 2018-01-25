# -*- coding: utf-8 -*-

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
		print(Board.current_player.initial+" Wins !")
		print("Player "+ PlayerA.initial + "’s frame number : " + str(playerA_score))
		print("Player "+ PlayerB.initial + "’s frame number : " + str(playerB_score))


		if playerA_score > playerB_score:
			PlayerA.num_wins += 1
		else:
			PlayerB.num_wins += 1
		return
	elif Board.tie():
		print("It's a tie")
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
	return (len(coordinate) == 3 and
			coordinate[0] in ["A","B","C","D","E","F","G","H","i","J","K","L","M","N","O","P","Q","R","S"][:Board.width] and
			coordinate[1] in ["0","1","2","3","4","5","6","7","8"][:Board.height] and
			coordinate[2] in ["E","W","N","S"][:Board.height])


def convert(coor):
	letter_dict = {"A":0, "B":1, "C": 2, "D": 3, "E": 4, "F": 5, "G": 6, "H": 7, "i": 8, "J": 9, "K": 10, "L": 11, "M": 12, "N": 13, "O": 14, "P": 15, "Q": 16, "R": 17, "S": 18, "T":19}
	reverse_dict = dict((reversed(item) for item in letter_dict.items()))

	coor = list(coor.upper())
	if coor[2] == "E":
		arr = []
		arr.append(letter_dict[coor[0]] + 1)
		arr.append(int(coor[1]))
		arr.append(letter_dict[coor[0]] + 1)
		arr.append(int(coor[1])+1)

	if coor[2] == "W":
		arr = []
		arr.append(letter_dict[coor[0]])
		arr.append(int(coor[1]))
		arr.append(letter_dict[coor[0]])
		arr.append(int(coor[1])+1)

	if coor[2] == "N":
		arr = []
		arr.append(letter_dict[coor[0]] )
		arr.append(int(coor[1]))
		arr.append(letter_dict[coor[0]] + 1)
		arr.append(int(coor[1]))

	if coor[2] == "S":
		arr = []
		arr.append(letter_dict[coor[0]] )
		arr.append(int(coor[1]) + 1)
		arr.append(letter_dict[coor[0]] + 1)
		arr.append(int(coor[1]) + 1)


	arr[0] = reverse_dict[arr[0]]
	arr[2] = reverse_dict[arr[2]]
	arr2 = ''.join([str(x) for x in arr])
	return arr2


def enter_coordinates():

	core = (raw_input("Player "+Board.current_player.initial+" please enter your coordinates : "  )).upper()
	letter_dict = {"A":0, "B":1, "C": 2, "D": 3, "E": 4, "F": 5, "G": 6, "H": 7, "i": 8, "J": 9, "K": 10, "L": 11, "M": 12, "N": 13, "O": 14, "P": 15, "Q": 16, "R": 17, "S": 18, "T":19}
	number_dict = {"1":0,"2":1,"3":2,"4":3,"5":4,"6":5,"7":6,"8":7}

	if valid_coordinate(core):
		coordinates = convert(core)
		first = list(coordinates[:2])
		first[0] = letter_dict[first[0]]
		first[1] = number_dict[first[1]]
		if valid_coordinate(core):
			second = list(coordinates[2:])
			second[0] = str(letter_dict[second[0]])
			second[1] = number_dict[second[1]]

			if not Board.set_line(first,second):
				print("Please enter an adjacent set of coordinates !!")
				enter_coordinates()
		else:
			print("Enter a valid coordinates !!")
			enter_coordinates()
	else:
		print("Enter a valid address !!")
		enter_coordinates()


def main():
	Board.board_setup()
	print("Please select a one letter name for player 1 : ")
	PlayerA.player_setup(" ")
	print("Please select a different one letter name for player 2 : ")
	PlayerB.player_setup(PlayerA.initial)
	Board.current_player = PlayerA
	Board.other_player = PlayerB
	play_game()
	
if __name__ == "__main__":
    main()