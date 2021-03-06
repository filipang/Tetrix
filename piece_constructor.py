import forms
import constants as cst
from random  import randint

class PieceConstructor:
    def __init__(self, background,board):
        self.background = background
        self.board=board
        self.queue = [self.gen(),self.gen(),self.gen(),self.gen()]
        self.display=[]
        self.display.append(self.queue[0]([3,3],self.background,self.board))
        self.display.append(self.queue[1]([3,7],self.background,self.board))
        self.display.append(self.queue[2]([3,11],self.background,self.board))
        self.display.append(self.queue[3]([3,16],self.background,self.board))
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
        self.display[0].delete(cst.GRAY)
        self.display=self.display[1:]
        self.display[0].moveWith(0,-4,False)
        self.display[1].moveWith(0,-4,False)
        self.display[2].moveWith(0,-4,False)
        piece = self.queue[0]
        self.queue = self.queue[1:]
        self.queue.append(self.gen())
        self.display.append(self.queue[3]([3,16],self.background,self.board))
        
        return piece
        