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
		print(Board.current_player.initial+" Kazandi !")
		print("Oyuncu "+ PlayerA.initial + "’e ait karelerin sayısı: " + str(playerA_score))
		print("Oyuncu "+ PlayerB.initial + "’e ait karelerin sayısı: " + str(playerB_score))


		if playerA_score > playerB_score:
			PlayerA.num_wins += 1
		else:
			PlayerB.num_wins += 1
		return
	elif Board.tie():
		print("Oyunu berabere.")
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
			coordinate[2] in ["D","B","K","G"][:Board.height])


def convert(coor):
	letter_dict = {"A":0, "B":1, "C": 2, "D": 3, "E": 4, "F": 5, "G": 6, "H": 7, "i": 8, "J": 9, "K": 10, "L": 11, "M": 12, "N": 13, "O": 14, "P": 15, "Q": 16, "R": 17, "S": 18, "T":19}
	reverse_dict = dict((reversed(item) for item in letter_dict.items()))

	coor = list(coor.upper())
	if coor[2] == "D":
		arr = []
		arr.append(letter_dict[coor[0]] + 1)
		arr.append(int(coor[1]))
		arr.append(letter_dict[coor[0]] + 1)
		arr.append(int(coor[1])+1)

	if coor[2] == "B":
		arr = []
		arr.append(letter_dict[coor[0]])
		arr.append(int(coor[1]))
		arr.append(letter_dict[coor[0]])
		arr.append(int(coor[1])+1)

	if coor[2] == "K":
		arr = []
		arr.append(letter_dict[coor[0]] )
		arr.append(int(coor[1]))
		arr.append(letter_dict[coor[0]] + 1)
		arr.append(int(coor[1]))

	if coor[2] == "G":
		arr = []
		arr.append(letter_dict[coor[0]] )
		arr.append(int(coor[1]) + 1)
		arr.append(letter_dict[coor[0]] + 1)
		arr.append(int(coor[1]) + 1)


	arr[0] = reverse_dict[arr[0]]
	arr[2] = reverse_dict[arr[2]]
	arr2 = ''.join([str(x) for x in arr])
	return arr2
	#print (arr2)


def enter_coordinates():
	#print("Oyuncu"+Board.current_player.initial+" lütfen tercihinizi giriniz: ")

	# if not Board.current_player.human:
	# 	isPlayerA = (Board.current_player == PlayerA)
	# 	move = Board.alphabeta_search(isPlayerA,PlayerA.score,PlayerB.score)
	# 	print(move)
	# 	Board.set_line(move[:2],move[2:])
	# 	return

	#print("Draw a line between adjacent dots by entering the dot coordinates")
	core = (raw_input("Oyuncu "+Board.current_player.initial+" lütfen tercihinizi giriniz: "  )).upper()
	#coordinates = convert(core)
	#print(coordinates)
	# if coordinates.upper() == "Q" or coordinates.upper() == "QUiT":
	# 	print("Goodbye!")
	# 	quit()
	letter_dict = {"A":0, "B":1, "C": 2, "D": 3, "E": 4, "F": 5, "G": 6, "H": 7, "i": 8, "J": 9, "K": 10, "L": 11, "M": 12, "N": 13, "O": 14, "P": 15, "Q": 16, "R": 17, "S": 18, "T":19}
	number_dict = {"1":0,"2":1,"3":2,"4":3,"5":4,"6":5,"7":6,"8":7}

	if valid_coordinate(core):
		coordinates = convert(core)
		print(coordinates)
		first = list(coordinates[:2])
		first[0] = letter_dict[first[0]]
		first[1] = number_dict[first[1]]
		if valid_coordinate(core):
			second = list(coordinates[2:])
			second[0] = str(letter_dict[second[0]])
			second[1] = number_dict[second[1]]

			if not Board.set_line(first,second):
				print("Aynı yeri girmeyin lütfen !!")
				enter_coordinates()
		else:
			print("Lutfen gecerli bir adres giriniz !!")
			enter_coordinates()
	else:
		print("Lutfen gecerli bir adres girinizfads !!")
		enter_coordinates()

	# elif len(coordinates) == 5:
	# 	split = coordinates.split()
	# 	if not coordinates[2] == " ":
	# 		print("Lutfen gecerli bir adres giriniz !!")
	# 		enter_coordinates()
	# 	elif valid_coordinate(split[0]):
	# 		first = split[0]
	# 		if valid_coordinate(split[1]):
	# 			second = split[1]
	# 			if not Board.set_line(first,second):
	# 				print("Lutfen koordinatlarin bitisik girin !!")
	# 				enter_coordinates()
	# 		else:
	# 			print("Lutfen gecerli bir adres giriniz !!")
	# 			enter_coordinates()
	# 	else:
	# 		print("Lutfen gecerli bir adres giriniz !!")
	# 		enter_coordinates()


	

def main():
	Board.board_setup()
	print("1. oyuncuyu temsil etmek icin bir karakter giriniz: ")
	PlayerA.player_setup(" ")
	print("2. oyuncuyu temsil etmek icin bir karakter giriniz: ")
	PlayerB.player_setup(PlayerA.initial)
	Board.current_player = PlayerA
	Board.other_player = PlayerB
	play_game()
	
if __name__ == "__main__":
    main()