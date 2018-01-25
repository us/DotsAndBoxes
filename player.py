# -*- coding: utf-8 -*-
class Player:
	initial = " "

	score = 0

	human = True

	search_depth = 0

	num_wins = 0

	def player_name(self, other_name):
		name = raw_input("")
		if name.upper() == "QUIT":
			print("Goodbye!")
			quit()
		if len(name) == 1 and not name == other_name and not name == " ":
			return name
		print("You must enter a different name !")
		return self.player_name(other_name)

	def human(self):
		self.human = True

	def player_setup(self, other_name):
		self.initial = self.player_name(other_name)
		self.human()