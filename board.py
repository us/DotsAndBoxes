# -*- coding: utf-8 -*-
import sys
import player
from random import shuffle

class Board:

	playerA = " "

	playerB = " "

	width = 0

	height = 0

	current_player = 0

	other_player = 0

	horiz_nums = ["    A","   B","   C","   D","   E","   F","   G","   H","   i","   J","   K","   L","   M","   N","   O","   P","   Q","   R","   S","   T"]

	depth = 0

	#moves_searched = 0


	lines = [["   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ",],
			 [" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "],
			 ["   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ",],
			 [" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "],
			 ["   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ",],
			 [" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "],
			 ["   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ",],
			 [" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "],
			 ["   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ",],
			 [" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "],
			 ["   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ",],
		 	 [" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "],
			 ["   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ",],
			 [" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "],
			 ["   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ",],
			 [" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "],
			 ["   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ",]
			 ]

	lines_drawn = [[False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False],
				  [False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False],
				  [False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False],
				  [False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False],
				  [False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False],
				  [False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False],
				  [False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False],
				  [False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False],
				  [False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False],
				  [False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False],
				  [False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False],
				  [False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False],
				  [False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False],
				  [False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False],
				  [False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False],
				  [False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False],
				  [False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False],
				  [False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False],
				  [False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False],
				  [False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False],
				  [False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False]]

	taken_by = [[" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "],
				[" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "],
				[" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "],
				[" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "],
				[" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "],
				[" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "],
				[" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "],
				[" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "],]



	def set_line(self, start, end):
		horiz = abs(int(start[0]) - int(end[0]))
		vert = abs(int(start[1]) - int(end[1]))
		if (horiz == 0 and vert == 1) or (horiz == 1 and vert == 0):
			if vert == 1:
				if not self.lines_drawn[2*min(int(start[1]),int(end[1]))+1][int(start[0])]:
					self.lines[2*min(int(start[1]),int(end[1]))+1][int(start[0])] = "|"
					self.lines_drawn[2*min(int(start[1]),int(end[1]))+1][int(start[0])] = True
					self.check_left_right(start,end)
				else:
					return False
			else:
				if not self.lines_drawn[2*int(start[1])][min(int(start[0]),int(end[0]))]:
					self.lines[2*int(start[1])][min(int(start[0]),int(end[0]))] = "---"
					self.lines_drawn[2*int(start[1])][min(int(start[0]),int(end[0]))] = True
					self.check_above_below(start,end)
				else:
					return False
			return True
		return False

	# def alphabeta_search(self,isPlayerA,playerAscore,playerBscore):
	# 	moves = self.generate_moves(self.lines_drawn)
	# 	best_move = moves[0]
	# 	best_score = -1000
	# 	self.depth = self.current_player.search_depth
	# 	for move in moves:
	# 		if self.depth == 0:
	# 			return move
	# 		self.moves_searched += 1
	# 		clone = self.next_state(move[:2],move[2:], self.lines_drawn, isPlayerA,playerAscore, playerBscore)
	# 		score = 0
	# 		if (not clone[1] - playerAscore == 0) or (not clone[2] - playerBscore == 0): #score change therefore continue to play max
	# 			#print("player not changed, keeping max alphabeta")
	# 			score = self.max_play(clone,playerAscore,playerBscore, isPlayerA, self.depth-1)
	# 		else:
	# 			score = self.min_play(clone,playerAscore,playerBscore, isPlayerA, self.depth-1, max_best_score = best_score)
	# 		if score > best_score:
	# 			best_move = move
	# 			best_score = score
	# 	return best_move

	# def min_play(self, state, old_scoreA, old_scoreB, originalPlayerA, depth, max_best_score = None):
	# 	end = (state[1] > self.width*self.height/2.0 or state[2] > self.width*self.height/2.0 or
	# 		  		(state[1] == state[2] and state[1]+ state[2] == self.width*self.height))
	# 	if end:
	# 		if originalPlayerA:
	# 			if state[1] > state[2]:
	# 				#print("score A > score B")
	# 				return 100
	# 			elif state[2] > state[1]:
	# 				#print("score B > score A")
	# 				return -100
	# 			else:
	# 				#print("Tie")
	# 				return 0
	# 		else:
	# 			if state[2] > state[1]:
	# 				#print("score B > score A")
	# 				return 100
	# 			elif state[1] > state[2]:
	# 				#print("score A > score B")
	# 				return -100
	# 			else:
	# 				#print("Tie")
	# 				return 0
	# 	elif depth == 0:
	# 		if originalPlayerA:
	# 			return state[1] - state[2]
	# 		else:
	# 			return state[2] - state[1]
	# 	moves = self.generate_moves(state[0])
	# 	best_score = 1000
	# 	for move in moves:
	# 		self.moves_searched += 1
	# 		isPlayerA = not state[3] #default swap players
	# 		if (not state[1] - old_scoreA == 0) or (not state[2] - old_scoreB == 0): #if a score changed keep same player
	# 			isPlayerA = state[3]
	# 		clone = self.next_state(move[:2],move[2:],state[0],isPlayerA,state[1],state[2])
	# 		score = 0
	# 		if (not clone[1] - state[1] == 0) or (not clone[2] - state[2] == 0): #kept the same player therefore keep playing min
	# 			score = self.min_play(clone, state[1], state[2], originalPlayerA, depth-1)
	# 			#print("player not changed, keeping min minplay")
	# 		else:
	# 			score = self.max_play(clone, state[1], state[2], originalPlayerA,depth-1,min_best_score = best_score)
	# 		#print("search score for this move is "+str(score))
	# 		if score < best_score:
	# 			best_score = score
	# 			if not max_best_score is None:
  	# 				if best_score <= max_best_score:
  	# 					#print("pruned")
  	# 					return best_score
    #
  	# 	return best_score

  	# def max_play(self,state,old_scoreA, old_scoreB, originalPlayerA, depth, min_best_score = None):
		# end = (state[1] > self.width*self.height/2.0 or state[2] > self.width*self.height/2.0 or
		# 	  		(state[1] == state[2] and state[1]+ state[2] == self.width*self.height))
		# if end:
		# 	if originalPlayerA:
		# 		if state[1] > state[2]:
		# 			#print("score A > score B")
		# 			return 100
		# 		elif state[2] > state[1]:
		# 			#print("score B > score A")
		# 			return -100
		# 		else:
		# 			#print("Tie")
		# 			return 0
		# 	else:
		# 		if state[2] > state[1]:
		# 			#print("score B > score A")
		# 			return 100
		# 		elif state[1] > state[2]:
		# 			#print("score A > score B")
		# 			return -100
		# 		else:
		# 			#print("Tie")
		# 			return 0
		# elif depth == 0:
		# 	if originalPlayerA:
		# 		return state[1] - state[2]
		# 	else:
		# 		return state[2] - state[1]
		# moves = self.generate_moves(state[0])
		# best_score = -1000
		# for move in moves:
		# 	self.moves_searched += 1
		# 	#print(move)
		# 	isPlayerA = not state[3] #default swap players
		# 	if (not state[1] - old_scoreA == 0) or (not state[2] - old_scoreB == 0): #if a score changed keep same player
		# 		isPlayerA = state[3]
		# 	clone = self.next_state(move[:2],move[2:],state[0],isPlayerA,state[1],state[2])
		# 	score = 0
		# 	if (not clone[1] - state[1] == 0) or (not clone[2] - state[2] == 0): #kept the same player therefore keep playing max
		# 		score = self.max_play(clone, state[1], state[2], originalPlayerA,depth-1)
		# 		#print("player not changed, keeping max maxplay")
		# 	else:
		# 		score = self.min_play(clone, state[1], state[2], originalPlayerA,depth-1,max_best_score = best_score)
		# 	if score > best_score:
		# 		best_score = score
		# 		if not min_best_score is None:
		# 			if best_score >= min_best_score:
		# 				#print("pruned")
		# 				return best_score
  	# 	return best_score

	def next_state(self,start,end,lines_drawn,isPlayerA,playerAscore, playerBscore):
		horiz = abs(int(start[0]) - int(end[0]))
		vert = abs(int(start[1]) - int(end[1]))
		cloned_lines_drawn = []
		for l in lines_drawn:
			cloned_lines_drawn.append(l[:])
		updated_A_score = playerAscore
		updated_B_score = playerBscore
		if vert == 1:
			cloned_lines_drawn[2*min(int(start[1]),int(end[1]))+1][int(start[0])] = True
			num_boxes = self.num_boxes_left_right(start,end,cloned_lines_drawn)
		else:
			cloned_lines_drawn[2*int(start[1])][min(int(start[0]),int(end[0]))] = True
			num_boxes = self.num_boxes_above_below(start,end,cloned_lines_drawn)
		if isPlayerA:
			updated_A_score += num_boxes
		else:
			updated_B_score += num_boxes
		return (cloned_lines_drawn, updated_A_score, updated_B_score, isPlayerA)

	def num_boxes_above_below(self,start,end,lines_drawn):
		num_boxes = 0
		if not int(start[1]) == self.height:
			if (lines_drawn[2*int(start[1])+2][min(int(start[0]),int(end[0]))] and
				lines_drawn[2*int(start[1])+1][min(int(start[0]),int(end[0]))] and
				lines_drawn[2*int(start[1])+1][min(int(start[0]),int(end[0]))+1]):
				num_boxes += 1

		if not start[1] == "0":
			if (lines_drawn[2*int(start[1])-2][min(int(start[0]),int(end[0]))] and
				lines_drawn[2*int(start[1])-1][min(int(start[0]),int(end[0]))] and
				lines_drawn[2*int(start[1])-1][min(int(start[0]),int(end[0]))+1]):
				num_boxes += 1

		return num_boxes

	def num_boxes_left_right(self,start,end,lines_drawn):
		num_boxes = 0
		if not int(start[0]) == self.width:
			if (lines_drawn[2*min(int(start[1]),int(end[1]))+1][int(start[0])+1] and
				lines_drawn[2*min(int(start[1]),int(end[1]))][int(start[0])] and
				lines_drawn[2*min(int(start[1]),int(end[1]))+2][int(start[0])]):
				num_boxes += 1

		if not start[0] == "0":
			if (lines_drawn[2*min(int(start[1]),int(end[1]))+1][int(start[0])-1] and
				lines_drawn[2*min(int(start[1]),int(end[1]))][int(start[0])-1] and
				lines_drawn[2*min(int(start[1]),int(end[1]))+2][int(start[0])-1]):
				num_boxes += 1

		return num_boxes

	def check_above_below(self,start,end):
		if not int(start[1]) == self.height:
			if (self.lines_drawn[2*int(start[1])+2][min(int(start[0]),int(end[0]))] and
				self.lines_drawn[2*int(start[1])+1][min(int(start[0]),int(end[0]))] and
				self.lines_drawn[2*int(start[1])+1][min(int(start[0]),int(end[0]))+1]):
				self.current_player.score += 1
				self.taken_by[int(start[1])][min(int(start[0]),int(end[0]))] = self.current_player.initial

		if not start[1] == "0":
			if (self.lines_drawn[2*int(start[1])-2][min(int(start[0]),int(end[0]))] and
				self.lines_drawn[2*int(start[1])-1][min(int(start[0]),int(end[0]))] and
				self.lines_drawn[2*int(start[1])-1][min(int(start[0]),int(end[0]))+1]):
				self.current_player.score += 1
				self.taken_by[int(start[1])-1][min(int(start[0]),int(end[0]))] = self.current_player.initial



	def check_left_right(self,start,end):
		if not int(start[0]) == self.width:
			if (self.lines_drawn[2*min(int(start[1]),int(end[1]))+1][int(start[0])+1] and
				self.lines_drawn[2*min(int(start[1]),int(end[1]))][int(start[0])] and
				self.lines_drawn[2*min(int(start[1]),int(end[1]))+2][int(start[0])]):
				self.current_player.score += 1
				self.taken_by[min(int(start[1]),int(end[1]))][int(start[0])] = self.current_player.initial

		if not start[0] == "0":
			if (self.lines_drawn[2*min(int(start[1]),int(end[1]))+1][int(start[0])-1] and
				self.lines_drawn[2*min(int(start[1]),int(end[1]))][int(start[0])-1] and
				self.lines_drawn[2*min(int(start[1]),int(end[1]))+2][int(start[0])-1]):
				self.current_player.score += 1
				self.taken_by[min(int(start[1]),int(end[1]))][int(start[0])-1] = self.current_player.initial


	def board_width(self):
		width = raw_input("Oyun alaninin sutun sayisini giriniz (3-19): ")
		# if width.upper() == "Q" or width.upper() == "QUiT":
		# 	print("Goodbye!")
		# 	quit()
		if width in ["3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19"]:
			return int(width)
		return self.board_width()


	# def generate_moves(self, lines_drawn):
	# 	moves = []
	# 	for x in range(self.width):
	# 		for y in range(self.height+1):
	# 			if not lines_drawn[2*y][x]:
	# 				moves.append(str(x)+str(y)+str(x+1)+str(y))
    #
	# 	for y in range(self.height):
	# 		for x in range(self.width+1):
	# 			if not lines_drawn[2*y+1][x]:
	# 				moves.append(str(x)+str(y)+str(x)+str(y+1))
	# 	shuffle(moves)
	# 	return moves






	def board_height(self):
		height = raw_input("Oyun alaninin satir sayisini giriniz (3-7): ")
		if height.upper() == "Q" or height.upper() == "QUiT":
			print("Goodbye!")
			quit()
		if height in ["3","4","5","6","7","8"]:
			return int(height)
		return self.board_height()


	def set_height(self, h):
		self.height = h


	def set_width(self, w):
		self.width = w

	def board_setup(self):
			print
			width = self.board_width()
			height = self.board_height() + 1
			self.set_width(width)
			self.set_height(height)

	def end_game(self):
		return self.current_player.score > self.width*self.height/2.0

	def tie(self):
		return (self.current_player.score == self.other_player.score and
				self.current_player.score + self.other_player.score == self.width*self.height)


	def print_board(self):
		
		horizontal = True
		line_num = 0
		for num in self.horiz_nums[:self.width]:
			sys.stdout.write(num)
		print
		for line in self.lines[:2*self.height-1]:
			if horizontal:
				sys.stdout.write("  ")
				sys.stdout.write(" o")
				line_num += 1
			else:
				sys.stdout.write(str(line_num))
				sys.stdout.write("  ")
			for l in range(len(line[:self.width+1])):
				sys.stdout.write((line[l]))
				if horizontal and not l == len(line[:self.width]):
					sys.stdout.write("o")
				elif not l == len(line[:self.width]):
					sys.stdout.write(" "+self.taken_by[line_num-1][l]+" ")
			horizontal = not horizontal
			
			print
		print


