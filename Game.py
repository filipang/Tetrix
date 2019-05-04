import pygame
import sys
import constants as cst
import block 
import forms
import piece_constructor
import time
from threading import Thread


    
    
def matrix(n,m):
    M=[]
    for i in range(n):
        M.append([])
        for j in range(m):
            if(i==0):
                M[i].append(0)
            else:
                M[i].append(None)

    return M  
    
class Tetris(Thread):
    def __init__(self):
        super(Tetris,self).__init__()
        self.setName("Tetris game Thread")
        self.screen = pygame.display.set_mode(cst.SIZE)
        self.background = pygame.Surface(self.screen.get_size())
        self.background.fill(cst.GRAY)  
        pygame.display.set_caption("Tetrix")
        self.foreground = pygame.Surface(cst.BOARD_SIZE)
        self.foreground.fill(cst.BLACK)
        self.blocks = matrix(cst.BLOCK_WIDTH+2, cst.BLOCK_HEIGHT+2)
        self.displayer=pygame.Surface(cst.DISPLAYER_SIZE)
        self.displayer.fill(cst.GRAY)
        self.ON=True   
        self.generator=piece_constructor.PieceConstructor(self.displayer,self.blocks)
        self.time_next=time.time()
        self.Levels=0

    def draw(self):
        self.screen.blit(self.background,(0,0))
        self.screen.blit(self.foreground,(cst.MARGIN,0))
        self.screen.blit(self.displayer,(cst.MARGIN+cst.BOARD_WIDTH,0))
        pygame.display.flip()
    
    def lock(self):
        if not self.currentForm.lock():
            return False 
        for i in range (1,cst.BLOCK_HEIGHT+1):
            if(self.blocks[0][i]==cst.BLOCK_WIDTH):
                self.Levels+=1
                self.blocks[0][i]=0
                for j in range (1,cst.BLOCK_WIDTH+1):
                    self.blocks[j][i].delete()
                    self.blocks[j][i]=None
                for j in range(i-1,0,-1):
                    self.blocks[0][j+1]=self.blocks[0][j]
                    for k in range(1,cst.BLOCK_WIDTH+1):
                        if self.blocks[k][j]!=None:
                            self.blocks[k][j].moveWith(0,1)
                            self.blocks[k][j+1]=self.blocks[k][j]
                        else:
                            self.blocks[k][j]=None
                        self.blocks[k][j]=None
        self.currentForm=self.generator.get_piece()([5,1],self.foreground,self.blocks)
        self.time_next=time.time()+cst.TIME_MAX
        return True
    
    def run(self):
        #s=forms.Line([3,3],cst.BLUE,self.foreground)
        #self.blocks[3][3]=block.Block(cst.GRAY,[3,3],False,self.foreground,self.blocks)
        #self.currentForm = forms.L1([5,2], self.foreground,self.blocks)
        self.currentForm=self.generator.get_piece()([5,1],self.foreground,self.blocks)
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
                        self.time_next=min(time.time()+cst.TIME_MAX,self.time_next+cst.TIME_ADD)
                        self.currentForm.rotate()

                    #UP w (DEBUGING FEATURE NOT BUG)
                    if(event.key==119):
                        self.currentForm.moveWith(0,-1)

                    if(event.key==32):
                        while(self.currentForm.moveWith(0,1)):
                            None
                        if not self.lock():
                            #GAME OVER
                            self.ON=False
                            print("GAME OVER")
                    #print (event.key)
                
            if(cst.GRAVITY and time.time()>=self.time_next):
                self.time_next=time.time()+cst.TIME_MAX
                if not self.currentForm.moveWith(0,1):#TRUE: a mutat
                    if not self.lock():
                        #GAME OVER
                        self.ON=False
                        print("GAME OVER")
                
            self.draw()


def main():
    game = Tetris()
    game.run()

if(__name__=="__main__"):
    main()

