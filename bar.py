# IMPORTS
import pygame

# THE CLASS

class Bar():

	pos_x = 0
	pos_y = 0
	width = 0
	height = 0

	def __init__(self, x, y, size):
		self.pos_x = x
		self.pos_y = y
		self.width = size*4
		self.height = size
		self.bar = pygame.Surface((self.width, self.height))

	def update_position(self, x):
		if (x != 0):
			self.pos_x = x
