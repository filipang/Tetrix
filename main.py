import pygame
import sys
import constants as cst
import block 

def exit():
    print("BYE")
    pygame.quit()
    sys.exit()

def init():
	pygame.init()
	screen = pygame.display.set_mode(cst.SIZE)
	pygame.display.set_caption("Tetrix")
	background = pygame.Surface(screen.get_size())

	background.fill(cst.BLACK)

	screen.blit(background,(0,0))
	pygame.display.flip()

	return background,screen

def run(background,screen):
	while True:
		for event in pygame.event.get():
			if (event.type == pygame.QUIT):
				exit()
			if(event.type==pygame.KEYDOWN):
				if(event.key==27):
					exit()
        
		screen.blit(background,(0,0))
		pygame.display.flip()

def main():
	background,screen = init()
	run(background,screen)

main()