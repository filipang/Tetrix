import pygame
import sys
import constants as cst
import block 
import forms

def exit():
    print("BYE") #debug
    pygame.quit()
    sys.exit()

class Tetris:
    def __init__(self):
        pygame.init()
        self.ON=True
        self.screen = pygame.display.set_mode(cst.SIZE)
        self.background = pygame.Surface(self.screen.get_size())
        self.background.fill(cst.GRAY)  
        self.foreground = pygame.Surface(cst.BOARD_SIZE)
        self.foreground.fill(cst.BLACK)
        pygame.display.set_caption("Tetrix")

    def draw(self):
        self.screen.blit(self.background,(0,0))
        self.screen.blit(self.foreground,(cst.MARGIN,cst.MARGIN))
        pygame.display.flip()

    def run(self):
        self.draw()
        #s=forms.Line([3,3],cst.BLUE,self.foreground)
        #b=block.Block(cst.BLUE,[3,3],False,self.foreground)
        #b.down()
        self.currentForm = forms.Square([0, 0], self.foreground)
        while self.ON:
            for event in pygame.event.get():
                if (event.type == pygame.QUIT):
                    self.ON=False
                    break;
                #ESC = exit()
                if(event.type==pygame.KEYDOWN):
                    if(event.key==27):
                        self.ON=False
                        break;
                    if(event.key==274):
                        #b.down()
                        self.currentForm.down()
                    if(event.key==275):
                        #b.right()
                        self.currentForm.right()
                    if(event.key==276):
                        #b.left()
                        self.currentForm.left()
                    #print (event.key)
        



            self.draw()
        ####
        exit()

def main():
    game = Tetris()
    game.run()
if("__main__"==__name__):
    main()