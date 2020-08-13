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
 
# ------------------------------- GLOBAL VARIABLES 
WINDOWWIDTH = 480
WINDOWHEIGHT = 600
# colors
BLACK = (0, 0, 0)
WHITE = (255, 0, 0)
 
MOVEMENT_STEP = 20
BAR_SIZE = 30

# create display window
DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
# pygame.display.set_caption('The Lonely Shooter')

def main(): 

	bar = Bar(WINDOWWIDTH/2 + BAR_SIZE, WINDOWHEIGHT * (6/7) , BAR_SIZE)

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
					if (bar.pos_x < WINDOWWIDTH - bar.width):
						bar.update_position(bar.pos_x + MOVEMENT_STEP)

				# move bar to the left of the screen
				if event.key == K_LEFT:
					# if the bar is not near the edge increment position
					if (bar.pos_x > 0):
						bar.update_position(bar.pos_x - MOVEMENT_STEP)

				# when the user presses the key 'q' quits the game
				if event.key == K_q:
					pygame.quit()
					sys.exit()
				 

		# draw/render 
		DISPLAYSURF.fill(WHITE)
		DISPLAYSURF.blit(bar.bar, (bar.pos_x, bar.pos_y))

		# done after drawing everything to the screen
		pygame.display.flip()

if __name__ == "__main__":
	main()