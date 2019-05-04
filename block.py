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

    def can(self,x,y):
        if x<=0 or x>cst.BLOCK_WIDTH or y>cst.BLOCK_HEIGHT:
            return False
        return (self.board[x][y]==None)

    def move(self,x,y,f=True):
        if(f):
            if(not(self.can(x,y))):
                return
            pygame.draw.rect(self.surface,cst.BLACK,self.rect)
        self.coords[0]=x;
        self.coords[1]=y;
        x,y = get_position(x,y)
        self.rect = pygame.Rect(x+1,y+1,cst.BLOCK_SIZE-1,cst.BLOCK_SIZE-1)
        pygame.draw.rect(self.surface,self.color,self.rect)

    def moveWith(self,x,y,f=True):
        x+=self.coords[0]
        y+=self.coords[1]
        self.move(x,y,f)

    def delete(self,color=cst.BLACK):
          pygame.draw.rect(self.surface,color,self.rect)

    def draw(self):
        pygame.draw.rect(self.surface,self.color,self.rect)
