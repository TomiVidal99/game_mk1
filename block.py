# IMPORTS
import pygame

# THE ACTUAL CLASS

class Block():

	destroy = False

	def __init__(self, x, y, size, color, max_hits, current_hits):
		self.x = x
		self.y = y
		self.width = size
		self.height = size
		self.color = color
		self.max_hits = max_hits
		self.current_hits = current_hits
		self.display = pygame.Surface((self.width, self.height))

	def update_color(self, new_color):
		# TODO: should check if the new_color is a valid property
		if True == True:
			self.color = new_color

	def update_hits(self):
		if self.current_hits < self.max_hits:
			self.current_hits += 1

	def destroy(self):
		self.destroy = True
