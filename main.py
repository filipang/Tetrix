import pygame
import sys
import constants as cst

pygame.init()

screen = pygame.display.set_mode(cst.SIZE)
pygame.display.set_caption("Tetrix")

background = pygame.Surface(screen.get_size())

background.fill(cst.RED)

screen.blit(background,(0,0))
pygame.display.flip()

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()

	background.fill(cst.GOLD)
	screen.blit(background,(0,0))
	pygame.display.flip()

