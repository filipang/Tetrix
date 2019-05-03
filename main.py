import pygame
import sys
import constants as cst
import block 
def exit():
    print("BYE")
    pygame.quit()
    sys.exit()
pygame.init()

screen = pygame.display.set_mode(cst.SIZE)
pygame.display.set_caption("Tetrix")

background = pygame.Surface(screen.get_size())

background.fill(cst.RED)

screen.blit(background,(0,0))
pygame.display.flip()
block2 = block.Block([255, 0, 255], [125, 75], 0, background)
block1 = block.Block([255, 255, 255], [100, 100], 0, background)

while True:
    for event in pygame.event.get():
        ################################# EXIT
        if (event.type == pygame.QUIT):
            exit()
        if(event.type==pygame.KEYDOWN):
            if(event.key==27):
                exit()
        ####################################

    #background.fill(cst.GOLD)
    screen.blit(background,(0,0))
    pygame.display.flip()


