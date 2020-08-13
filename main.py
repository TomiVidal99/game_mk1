# import necessary packages
import pygame, sys
from pygame import *
 
pygame.init() # initialize pygame
 
WINDOWWIDTH = 480
WINDOWHEIGHT = 600
 
# colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
 
# create display window
DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
pygame.display.set_caption('The Lonely Shooter')
 


def main(): 
	barrita = pygame.Surface((50, 50))
	barrita_x = 0
	barrita_y = 0
	# loop pricipal
	while True:
		barrita_x = barrita_x + 0.01
		barrita_y = barrita_y + 0.01
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()
		# draw/render 
		DISPLAYSURF.fill(WHITE)
		DISPLAYSURF.blit(barrita, (barrita_x, barrita_y))
		
		# done after drawing everything to the screen
		pygame.display.flip()

if __name__ == "__main__":
	main()