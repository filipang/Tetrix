import pygame
import constants as cst


def get_position(x, y):
	x = cst.BLOCK_SIZE*x
	y = cst.BLOCK_SIZE*y
	return x,y

class Block:
    def __init__(self, color, coords, fixed, surface):
        self.color = color
        self.coords = coords
        self.fixed = fixed
        self.surface=surface
        x,y = get_position(coords[0],coords[1])
        self.rect = pygame.Rect(x+1,y+1,cst.BLOCK_SIZE-1,cst.BLOCK_SIZE-1)
        pygame.draw.rect(surface, color, self.rect)
    def down(self,nr=1,f=True):
        if(f):
            pygame.draw.rect(self.surface, cst.BLACK, self.rect)
        self.coords[1]+=1
        x,y = get_position(0,1)
        self.rect.move_ip(x,y)
        pygame.draw.rect(self.surface, self.color, self.rect)
        
    def left(self,nr=1,f=True):
        if(f):
            pygame.draw.rect(self.surface, cst.BLACK, self.rect)
        self.coords[0]-=1
        x,y = get_position(-1,0)
        self.rect.move_ip(x,y)
        pygame.draw.rect(self.surface, self.color, self.rect)
        
    def right(self,nr=1,f=True):
        if(f):
            pygame.draw.rect(self.surface, cst.BLACK, self.rect)
        self.coords[0]+=1
        x,y = get_position(1,0)
        self.rect.move_ip(x,y)
        pygame.draw.rect(self.surface, self.color, self.rect)
        
    