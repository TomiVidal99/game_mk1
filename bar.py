# IMPORTS
import pygame

# THE CLASS

class Bar():

	def __init__(self, x, y, width, height, color):
		self.x = x
		self.y = y
		self.width = width
		self.height = height
		self.color = color
		self.display = pygame.Surface((self.width, self.height))

	def update_position(self, x):
		if x != 0:
			self.x = x

	def update_width(self, new_width):
		self.width = new_width