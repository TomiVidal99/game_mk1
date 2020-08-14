# import necessary packages
import pygame, sys
from pygame import *
from bar import Bar
from block import Block
from ball import Ball

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

# colors
LIGHT_BLUE = (29, 124, 145)
BLACK = (0, 0, 0)
WHITE = (255, 0, 0)
RED = (226, 63, 27)
ORANGE = (221, 121, 13)
GREEN = (31, 224, 13)
 
# bar
MOVEMENT_STEP = 20
BAR_SIZE = 30

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

# MAIN FUNCTION
def main(): 

	# creates the bar object
	bar = Bar(WINDOWWIDTH/2 - 2*BAR_SIZE, WINDOWHEIGHT * (6/7) , BAR_SIZE, RED)

	# creates the ball object
	ball = Ball(WINDOWWIDTH/2, WINDOWHEIGHT, 50, WHITE, 0.1, 0, -1)

	#create all the blocks objects
	blocks = []
	print(BLOCKS_COLUMNS)
	for i in range(BLOCKS_ROWS):
		for j in range(BLOCKS_COLUMNS):
			if j < BLOCKS_COLUMNS:
				pos_x = j*BLOCKS_SIZE+(j+1)*BLOCKS_SEPARATION_X
				pos_y = i*BLOCKS_SIZE+(i+1)*BLOCKS_SEPARATION_Y
				blocks.insert(j*(i+1), Block(pos_x, pos_y, BLOCKS_SIZE, BLOCKS_INITIAL_COLOR, BLOCKS_MAX_HITS, 0))

	# loop pricipal
	while True:

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

				# when the user presses the key 'q' quits the game
				if event.key == K_q:
					pygame.quit()
					sys.exit()

		# draw/render 
		DISPLAY.fill(BACKGROUND_COLOR)

		# draw bar
		bar.display.fill(bar.color)
		DISPLAY.blit(bar.display, (bar.x, bar.y))

		# check collition of ball with the edges
		vertical_distance_bar_ball = ( (bar.y - ball.y) ** 2 ) ** 0.5
		if (ball.x + ball.size/2) >= WINDOWWIDTH:
			ball.update_direction(-1, 0)
		if (ball.x - ball.size/2) <= 0:
			ball.update_direction(1, 0)
		if (ball.y + ball.size/2) >= WINDOWHEIGHT or vertical_distance_bar_ball <= (ball.size/2 + bar.height/2):
			ball.update_direction(0, -1)
		if (ball.y - ball.size/2) <= 0:
			ball.update_direction(0, 1)

		# draw ball
		pos_x = ball.x + (ball.direction_x * ball.velocity)
		pos_y = ball.y + (ball.direction_y * ball.velocity)
		ball.update_position(pos_x, pos_y)
		ball.display.fill(ball.color)
		DISPLAY.blit(ball.display, (ball.x, ball.y))

		print("ball pos: ", ball.x, ball.y, ball.velocity)

		#draw all the blocks objects
		for block in blocks:
			horizontal_distance = ( (ball.x - block.x  ) ** 2 ) ** 0.5
			if horizontal_distance > (ball.size/2 + block.height/2):	
				#block.display.fill(block.color)
				DISPLAY.blit(block.display, (block.x, block.y))
			else:
				print(horizontal_distance)
				print("should be removed")
				# blocks.remove(blocks)

		# done after drawing everything to the screen
		pygame.display.flip()

if __name__ == "__main__":
	main()