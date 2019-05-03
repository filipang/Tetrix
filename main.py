import pygame
import sys
import constants as cst
import block 

def exit():
    print("BYE") #debug
    pygame.quit()
    sys.exit()

class Tetris:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(cst.SIZE)
        self.background = pygame.Surface(self.screen.get_size())
        self.background.fill(cst.GRAY)  
        pygame.display.set_caption("Tetrix")

    def draw(self):
        foreground = pygame.Surface(cst.BOARD_SIZE)
        foreground.fill(cst.BLACK)
        self.screen.blit(self.background,(0,0))
        self.screen.blit(foreground,(cst.MARGIN,cst.MARGIN))
        pygame.display.flip()
        
    def run(self):
        self.draw()
<<<<<<< HEAD
        while True:
=======
        s=forms.Line([3,3],cst.BLUE,self.foreground)
        #b=block.Block(cst.BLUE,[3,3],False,self.foreground)
        while self.ON:
>>>>>>> parent of 3736848... Moves
            for event in pygame.event.get():
                if (event.type == pygame.QUIT):
                    exit()
                #ESC = exit()
                if(event.type==pygame.KEYDOWN):
                    if(event.key==27):
<<<<<<< HEAD
                        exit()
=======
                        self.ON=False
                        break;
>>>>>>> parent of 3736848... Moves
        



            self.draw()

def main():
    game = Tetris()
    game.run()

main()