# import necessary packages
import pygame, sys
from pygame import *
from bar import Bar

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
 
# GLOBAL VARIABLES 

# colors
LIGHT_BLUE = (29, 124, 145)
BLACK = (0, 0, 0)
WHITE = (255, 0, 0)
RED = (226, 63, 27)
ORANGE = (221, 121, 13)
GREEN = (31, 224, 13)
 
MOVEMENT_STEP = 20
BAR_SIZE = 30

WINDOWWIDTH = 480
WINDOWHEIGHT = 600

BACKGROUND_COLOR = LIGHT_BLUE
WINDOW_TITLE = "GAME_MK1"

# create display window and sets the title
DISPLAY = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
pygame.display.set_caption(WINDOW_TITLE)

def main(): 

	bar = Bar(WINDOWWIDTH/2 + BAR_SIZE, WINDOWHEIGHT * (6/7) , BAR_SIZE, RED)

	# loop pricipal
	while True:

		# update position
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
		bar.bar.fill(bar.color)
		DISPLAY.blit(bar.bar, (bar.x, bar.y))

		# done after drawing everything to the screen
		pygame.display.flip()

if __name__ == "__main__":
	main()