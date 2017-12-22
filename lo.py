
def sik(coor):
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

	print (arr2)


sik("a0g")







