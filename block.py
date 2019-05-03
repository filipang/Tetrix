import pygame
import constants as cst


def get_position(x, y):
	x = cst.BLOCK_SIZE*x + cst.MARGIN
	y = cst.BLOCK_SIZE*y + cst.MARGIN
	return x,y

class Block:
    def __init__(self, color, coords, fixed, surface):
        self.color = color
        self.coords = coords
        self.fixed = fixed
        x,y = get_position(coords[0],coords[1])
        self.rect = pygame.Rect(x,y,cst.BLOCK_SIZE-1,cst.BLOCK_SIZE-1)
        pygame.draw.rect(surface, color, self.rect)

    