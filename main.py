import pygame
import sys
import constants as cst
import block 
import forms

def exit():
    print("BYE") #debug
    pygame.quit()
    sys.exit()
    
    
def matrix(n,m):
    M=[]
    for i in range(n):
        M.append([])
        for j in range(m):
            M[i].append(None)

    return M  
    
class Tetris:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(cst.SIZE)
        self.background = pygame.Surface(self.screen.get_size())
        self.background.fill(cst.GRAY)  
        pygame.display.set_caption("Tetrix")
        self.foreground = pygame.Surface(cst.BOARD_SIZE)
        self.foreground.fill(cst.BLACK)
        self.blocks = matrix(cst.BLOCK_WIDTH+2, cst.BLOCK_HEIGHT+2)
        #print (self.blocks)

    def draw(self):
        self.screen.blit(self.background,(0,0))
        self.screen.blit(self.foreground,(cst.MARGIN,0))
        pygame.display.flip()
        
    def run(self):
        #s=forms.Line([3,3],cst.BLUE,self.foreground)
        self.blocks[3][3]=block.Block(cst.BLUE,[3,3],False,self.foreground,self.blocks)
        self.ON = True
        self.currentForm = forms.L1([2,2], self.foreground,self.blocks)
        self.draw()
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
                    #DOWN arrow down
                    if(event.key==274):
                        self.currentForm.moveWith(0,1)

                    #RIGHT arrow right
                    if(event.key==275):
                        self.currentForm.moveWith(1,0)

                    #LEFT arrow left
                    if(event.key==276):
                        self.currentForm.moveWith(-1,0)

                    #ROTATE arrow up
                    if(event.key==273):
                        self.currentForm.rotate()

                    #UP w (DEBUGING FEATURE NOT BUG)
                    if(event.key==119):
                        self.currentForm.moveWith(0,-1)

                    #print (event.key)
            self.draw()
        exit()
        

def main():
    game = Tetris()
    game.run()

main()
