import pygame
import constants as cst


def get_position(x, y):
	x = cst.BLOCK_SIZE*(x-1)
	y = cst.BLOCK_SIZE*(y-1)
	return x,y

class Block:
    def __init__(self, color, coords, fixed, surface,board):
        self.color = color
        self.coords = coords.copy()
        self.board=board
        self.fixed = fixed
        self.surface = surface
        x,y = get_position(coords[0],coords[1])
        self.rect = pygame.Rect(x+1,y+1,cst.BLOCK_SIZE-1,cst.BLOCK_SIZE-1)
        pygame.draw.rect(surface, color, self.rect)

    def down(self,nr=1,f=True):
        if(f):
            if(not self.can_down()):
                return
            pygame.draw.rect(self.surface, cst.BLACK, self.rect)
        self.coords[1]+=1
        x,y = get_position(1,2)
        self.rect.move_ip(x,y)
        pygame.draw.rect(self.surface, self.color, self.rect)

    def can_down(self):
        return not self.board[self.coords[0]][self.coords[1]+1]
        
    def left(self,nr=1,f=True):
        if(f):
            if(not self.can_left()):
                return
            pygame.draw.rect(self.surface, cst.BLACK, self.rect)
        self.coords[0]-=1
        x,y = get_position(0,1)
        self.rect.move_ip(x,y)
        pygame.draw.rect(self.surface, self.color, self.rect)

    def can_left(self):
        return not self.board[self.coords[0]-1][self.coords[1]]
        
    def right(self,nr=1,f=True):
        if(f):
            if(not self.can_right()):
                return
            pygame.draw.rect(self.surface, cst.BLACK, self.rect)
        self.coords[0]+=1
        x,y = get_position(2,1)
        self.rect.move_ip(x,y)
        pygame.draw.rect(self.surface, self.color, self.rect)
        

    def can_right(self):
        return not self.board[self.coords[0]+1][self.coords[1]]
