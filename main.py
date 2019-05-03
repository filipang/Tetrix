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
            M[i].append(False)
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
        for i in range(cst.BLOCK_WIDTH+2):
            self.blocks[i][0] = True
            self.blocks[i][cst.BLOCK_HEIGHT+1] = True
        for i in range(cst.BLOCK_HEIGHT+2):
            self.blocks[0][i] = True
            self.blocks[cst.BLOCK_WIDTH+1][i] = True
        #print (self.blocks)

    def draw(self):
        self.screen.blit(self.background,(0,0))
        self.screen.blit(self.foreground,(cst.MARGIN,0))
        pygame.display.flip()
        
    def run(self):
        #s=forms.Line([3,3],cst.BLUE,self.foreground)
        #b=block.Block(cst.BLUE,[3,3],False,self.foreground)
        self.ON = True
        self.currentForm = forms.Square([1, 1], self.foreground,self.blocks)
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
        exit()
        

def main():
    game = Tetris()
    game.run()

main()
