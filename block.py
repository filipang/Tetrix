# -*- coding: utf-8 -*-
"""
Created on Fri May  3 14:35:07 2019

@author: User
"""
import pygame
class Block:
    def __init__(self, color, position, fixed, surface):
        self.color = color
        self.position = position
        self.fixed = fixed
        self.rect = pygame.Rect(position[0],position[1], 50, 50)
        pygame.draw.rect(surface, color, self.rect)
        #print("Hallelujah!")
        