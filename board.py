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

	horiz_nums = ["     A","   B","   C","   D","   E","   F","   G","   H","   i","   J","   K","   L","   M","   N","   O","   P","   Q","   R","   S","   T"]

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
		width = raw_input("Please enter a board width between 1 and 19 : ")

		if width in ["3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19"]:
			return int(width)
		return self.board_width()


	def board_height(self):
		height = raw_input("Please enter a board height between 1 and 9 : ")
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
		return self.current_player.score > (self.width)*(self.height-1)/2.0

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
# a1b
# a2b
# a3b
# a1d
# b2d
# b3d
# b1g
# a2g
# a3g
# a1k
# a3d
# a1g
# c1d
# b2g
# c1k
# a2d
# c2d
# a2k
# b3g
# c3d
# c1g
# a3k
# b1d
# c3g
# b1k
# b2k
# b3k
# c2g
