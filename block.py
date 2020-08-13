# IMPORTS


# THE ACTUAL CLASS

class Block():

	amount_of_hits = 0

	def __init__(self, x, y, size, color):
		self.x = x
		self.y = y
		self.width = size
		self.height = size
		self.color = color

	def update_color(self, new_color):
		# TODO: should check if the new_color is a valid property
		if (True == True):
			self.color = new_color

	def update_hits(self):
		if (self.amount_of_hits < 3):
			self.amount_of_hits += 1
