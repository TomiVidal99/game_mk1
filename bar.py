# IMPORTS
import pygame

# THE CLASS

class Bar():

	def __init__(self, x, y, size, color):
		self.x = x
		self.y = y
		self.width = size*4
		self.height = size
		self.color = color
		self.bar = pygame.Surface((self.width, self.height))

	def update_position(self, x):
		if (x != 0):
			self.x = x
