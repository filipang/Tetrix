# -*- coding: utf-8 -*-
"""
Created on Sat May  4 01:32:34 2019

@author: User
"""


class PieceConstructor:
    def __init__(self, background):
        self.background = background
        self.queue = [self.gen(),self.gen(),self.gen(),self.gen()]
        
    def gen(self):
        x = randint(0, 6)
        piece = None
        if x == 0:
            piece = forms.Square
        if x == 1:
            piece = forms.L1
        if x == 2:
            piece = forms.L2
        if x == 3:
            piece = forms.Fulger1
        if x == 4:
            piece = forms.Fulger2
        if x == 5:
            piece = forms.Line
        if x == 6:
            piece = forms.T
        return piece
    
    def get_piece(self):
        
        piece = self.queue[0]
        self.queue = self.queue[1:]
        self.append(self.gen())
        