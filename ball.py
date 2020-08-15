# IMPORTS
import pygame

# THE CLASS

class Ball():

	def __init__(self, x, y, radius, color, velocity, direction_x, direction_y):
		self.x = x
		self.y = y
		self.radius = radius
		self.color = color
		self.velocity = velocity
		self.direction_x = direction_x
		self.direction_y = direction_y
		self.display = pygame.Surface((self.radius*2, self.radius*2))

	def update_position(self, x, y):
		if x != 0:
			self.x = x
		if y != 0:
			self.y = y

	def update_color(self, new_color):
		self.color = new_color

	def update_direction(self, new_direction_x, new_direction_y):
		if new_direction_x != 0:
			self.direction_x = new_direction_x
		if new_direction_y != 0:
			self.direction_y = new_direction_y

	def update_velocity(self, new_velocity):
		self.velocity = new_velocity 