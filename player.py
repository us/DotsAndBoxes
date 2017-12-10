class Player:
	initial = " "

	score = 0

	human = True

	search_depth = 0

	num_wins = 0

	def player_name(self, other_name):
		name = raw_input("Name: ")
		if name.upper() == "QUIT":
			print("Goodbye!")
			quit()
		if len(name) == 1 and not name == other_name and not name == " ":
			return name
		print("You Must Enter a Different Name")
		return self.player_name(other_name)

	def human(self):
		human = raw_input("Is This A Human? (Y/N): ")
		if human.upper() == "Q" or human.upper() == "QUIT":
			print("Goodbye!")
			quit()
		if human.capitalize() == "Y":
			self.human = True
		elif human.capitalize() == "N":
			self.human = False
			self.set_depth()
		else:
			print("Please Enter Y or N")
			return self.human()

	def set_depth(self):
		depth = raw_input("Please Enter a Search Depth between 0 and 5: ")
		if depth.upper() == "Q" or depth.upper() == "QUIT":
			print("Goodbye!")
			quit()
		if depth in ["0","1","2","3","4","5"]:
			self.search_depth = int(depth)
		else:
			self.set_depth()

	def player_setup(self, other_name):
		self.initial = self.player_name(other_name)
		self.human()