# import necessary packages
import pygame, sys
from pygame import *
from bar import Bar
from block import Block
from ball import Ball
import numpy as np
import random
from fontTools.ttLib import TTFont

from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)
 
pygame.init() # initialize pygame
 
# GLOBAL VARIABLES ------------------------

# fonts
MAIN_FONT = 'always forever.ttf'

GAME_DIFFICULTIES = ['EASY', 'MEDIUM', 'HARD']
GAME_DIFFICULTY = GAME_DIFFICULTIES[1]

# colors
LIGHT_BLUE = (29, 124, 145)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
ORANGE = (221, 121, 13)
GREEN = (31, 224, 13)
 
# bar
MOVEMENT_STEP = 20
BAR_WIDTH_EASY = 160
BAR_WIDTH_MEDIUM = 100
BAR_WIDTH_HARD = 60
BAR_WIDTH = BAR_WIDTH_MEDIUM
BAR_HEIGHT = 10

#ball
BALL_RADIUS = 5
BALL_VELOCITY_EASY = 0.05
BALL_VELOCITY_MEDIUM = 0.15
BALL_VELOCITY_HARD = 0.25
BALL_VELOCITY = BALL_VELOCITY_MEDIUM

# screen
WINDOWWIDTH = 480
WINDOWHEIGHT = 600
BACKGROUND_COLOR = LIGHT_BLUE
WINDOW_TITLE = "GAME_MK1"
# create display window and sets the title
DISPLAY = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
pygame.display.set_caption(WINDOW_TITLE)

# blocks
BLOCKS_AMOUNT = 180
BLOCKS_ROWS = 10
BLOCKS_COLUMNS = int(BLOCKS_AMOUNT / BLOCKS_ROWS)
BLOCKS_SIZE = 10
BLOCKS_SEPARATION_X = 15
BLOCKS_SEPARATION_Y = 5
BLOCKS_INITIAL_COLOR = GREEN
BLOCKS_SECONDARY_COLOR = ORANGE
BLOCKS_THIRD_COLOR = RED
BLOCKS_MAX_HITS = 3

# ------------------------

def change_difficulty():
	global BALL_VELOCITY, BAR_WIDTH, GAME_DIFFICULTY
	if GAME_DIFFICULTY == GAME_DIFFICULTIES[0]:
		GAME_DIFFICULTY = GAME_DIFFICULTIES[1]
		BALL_VELOCITY = BALL_VELOCITY_MEDIUM
		BAR_WIDTH = BAR_WIDTH_MEDIUM
	elif GAME_DIFFICULTY == GAME_DIFFICULTIES[1]:
		GAME_DIFFICULTY = GAME_DIFFICULTIES[2]
		BALL_VELOCITY = BALL_VELOCITY_HARD
		BAR_WIDTH = BAR_WIDTH_HARD
	elif GAME_DIFFICULTY == GAME_DIFFICULTIES[2]:
		GAME_DIFFICULTY = GAME_DIFFICULTIES[0]
		BALL_VELOCITY = BALL_VELOCITY_EASY
		BAR_WIDTH = BAR_WIDTH_EASY
	ball.update_velocity(BALL_VELOCITY)
	bar.update_width(BAR_WIDTH)
	create_init_configuration()

# when the user has pressed a key o click something
def handle_user_events():
	# counts all the events that occured
		for event in pygame.event.get():

			# when the user click the quit button, exits the game
			if event.type == QUIT:
				pygame.quit()
				sys.exit()

			# when press keys
			if event.type == KEYDOWN:

				# move bar to the right of the screen
				if event.key == K_RIGHT:
					# if the bar is not near the edge increment position
					if (bar.x < WINDOWWIDTH - bar.width):
						bar.update_position(bar.x + MOVEMENT_STEP)

				# move bar to the left of the screen
				if event.key == K_LEFT:
					# if the bar is not near the edge increment position
					if (bar.x > 0):
						bar.update_position(bar.x - MOVEMENT_STEP)

				# when the user presses the key 'r' restarts the game
				if event.key == K_r:
					print("Restarted")
					create_init_configuration()

				# when the user presses the key 'd' changes the game's difficulty
				if event.key == K_d:
					print("Difficulty changed")
					change_difficulty()

				# when the user presses the key 'q' quits the game
				if event.key == K_q:
					pygame.quit()
					sys.exit()

def text(surface, size, x, y, text, color):
    font = pygame.font.Font(MAIN_FONT, size)
    text = font.render(text, 1, color)
    surface.blit(text, (x, y))

def display_difficulty():
	text(DISPLAY, 14, 0, 0, GAME_DIFFICULTY, BLACK)

def create_init_configuration():
	# creates the bar object
	global bar, ball, blocks

	# make a random 
	r1 = random.random()
	r2 = random.random()
	direction_x, direction_y = 0, 0
	if r1 < 0.5:
		direction_x = -1
	else:
		direction_x = 1
	if r2 < 0.5:
		direction_y = -1
	else:
		direction_y = 1

	bar = Bar( ( (WINDOWWIDTH/2) - (BAR_WIDTH/2) ), ( WINDOWHEIGHT * (7/8) ) , BAR_WIDTH, BAR_HEIGHT, RED)
	# creates the ball object
	ball = Ball(WINDOWWIDTH/2 - 25, WINDOWHEIGHT/3, BALL_RADIUS, WHITE, BALL_VELOCITY, direction_x, direction_y)
	#create all the blocks objects
	blocks = []
	for i in range(BLOCKS_ROWS):
		for j in range(BLOCKS_COLUMNS):
			if j < BLOCKS_COLUMNS:
				pos_x = j*BLOCKS_SIZE+(j+1)*BLOCKS_SEPARATION_X
				pos_y = i*BLOCKS_SIZE+(i+1)*BLOCKS_SEPARATION_Y
				blocks.insert(j*(i+1), Block(pos_x, pos_y, BLOCKS_SIZE, BLOCKS_INITIAL_COLOR, BLOCKS_MAX_HITS, 0))

# MAIN FUNCTION
def main(): 

	# displays the game difficulty at the top left
	display_difficulty()

	# creates the ball, bar and blocks, as global variables
	create_init_configuration()
	
	# loop pricipal
	while True:

		# check user events
		handle_user_events()
		
		# draw/render 
		DISPLAY.fill(BACKGROUND_COLOR)

		# draw bar
		bar.display.fill(bar.color)
		DISPLAY.blit(bar.display, (bar.x, bar.y))

		# check collition of ball with the edges
		vertical_distance_bar_ball = np.absolute((bar.y - ball.y))
		if (ball.x + ball.radius) >= WINDOWWIDTH:
			ball.update_direction(-1, 0)
		if (ball.x) <= 2:
			ball.update_direction(1, 0)
		if (ball.y) <= 2:
			ball.update_direction(0, 1)
		if vertical_distance_bar_ball <= ball.radius and (ball.x - ball.radius + 5) >= bar.x and (ball.x + ball.radius - 5) <= (bar.x + bar.width):
			ball.update_direction(0, -1)
		if (ball.y) >= (WINDOWHEIGHT - ball.radius): # HITS THE FLOOR
			ball.velocity = 0
			text(DISPLAY, 80, WINDOWWIDTH/3 - 80, WINDOWHEIGHT/2 - 80, 'You have LOST!', RED)
			text(DISPLAY, 30, WINDOWWIDTH/3 - 30, WINDOWHEIGHT/2 + 50, 'Press [R] to restart or [Q] to quit', BLACK)

		# draw ball
		pos_x = ball.x + (ball.direction_x * ball.velocity)
		pos_y = ball.y + (ball.direction_y * ball.velocity)
		ball.update_position(pos_x, pos_y)
		ball.display.fill(ball.color)

		DISPLAY.blit(ball.display, (ball.x, ball.y))

		#ball.velocity += 0.000005

		#print("ball pos: ", ball.x, ball.y, ball.velocity)

		# draw all the blocks objects
		if ball.velocity != 0:
			for block in blocks:
				#DISPLAY.blit(block.display, (block.x, block.y))
				#horizontal_distance = ( (ball.x - block.x  ) ** 2 ) ** 0.5
				horizontal_distance = np.absolute(ball.x - block.x)
				vertical_distance = np.absolute(ball.y - block.y)
				if horizontal_distance <= (ball.radius + block.width/2) and vertical_distance <= (ball.radius + block.height/2):	
					# make the ball bounce off
					ball.bounce()
					# update the color and the hits of the block
					block.update_hits()
					if block.current_hits == 1:
						block.update_color(BLOCKS_SECONDARY_COLOR)
					elif block.current_hits == 2:
						block.update_color(BLOCKS_THIRD_COLOR)
					else:
						blocks.pop(blocks.index(block))
					# increase ball velocity
					ball.update_velocity(ball.velocity + 0.02)
				else:
					block.display.fill(block.color)
					DISPLAY.blit(block.display, (block.x, block.y))

		# done after drawing everything to the screen
		pygame.display.flip()

if __name__ == "__main__":
	main()