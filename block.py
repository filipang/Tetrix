import pygame
import constants as cst


def get_position(x, y):
<<<<<<< HEAD
	pos_x = cst.BLOCK_SIZE*x + cst.MARGIN
	pos_y = cst.BLOCK_SIZE*y + cst.MARGIN
=======
	x = cst.BLOCK_SIZE*x + cst.MARGIN
	y = cst.BLOCK_SIZE*y + cst.MARGIN
>>>>>>> parent of 3736848... Moves
	return x,y

class Block:
    def __init__(self, color, coords, fixed, surface):
        self.color = color
        self.coords = coords
        self.fixed = fixed
        x,y = get_position(coords[0],coords[1])
<<<<<<< HEAD
        self.rect = pygame.Rect(x,y,cst.BLOCK_SIZE,cst.BLOCK_SIZE)
=======
        self.rect = pygame.Rect(x,y,cst.BLOCK_SIZE-1,cst.BLOCK_SIZE-1)
>>>>>>> parent of 3736848... Moves
        pygame.draw.rect(surface, color, self.rect)

    