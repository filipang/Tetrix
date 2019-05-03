import block
import pygame
import constants as cst

class Form:
    def __init__(self,center,color,surface,board):
        self.center=center.copy()
        self.surface=surface
        self.color=color
        self.board = board
        self.blocks=[]     

    def down(self,nr=1):
        #print(len(self.blocks))
        ok = False
        for b in self.blocks:
            if not b.can_down():
                return
        self.center[1]+=nr
        for b in self.blocks:
            pygame.draw.rect(b.surface, cst.BLACK, b.rect)
        for b in self.blocks:
            b.down(nr,False)

    def left(self,nr=1):
        #print(len(self.blocks))
        ok = False
        for b in self.blocks:
            if not b.can_left():
                return
        self.center[0]-=nr;
        for b in self.blocks:
            pygame.draw.rect(b.surface, cst.BLACK, b.rect)
        for b in self.blocks:
            b.left(nr,False)

    def right(self,nr=1):
        #print(len(self.blocks))
        ok = False
        for b in self.blocks:
            if not b.can_right():
                return
        self.center[0]+=nr;
        for b in self.blocks:
            pygame.draw.rect(b.surface, cst.BLACK, b.rect)
        for b in self.blocks:
            b.right(nr,False)
        
    def rotate(self): #clock-wise rotation

        for b in self.blocks:
            x = b.coords[0]
            y = b.coords[1]
            center_x = self.center[0]
            center_y = self.center[1]
            x = x - center_x
            y = y - center_y
            new_x = center_x - y
            new_y = center_y + x
            if not(b.can(new_x,new_y)):
                return

        for b in self.blocks:
            b.delete()

        for b in self.blocks:
            x = b.coords[0]
            y = b.coords[1]
            center_x = self.center[0]
            center_y = self.center[1]
            x = x - center_x
            y = y - center_y
            new_x = center_x - y
            new_y = center_y + x

            b.move(center_x-y,center_y+x,False)


class Square(Form):
    def __init__(self,center,surface, board):
        Form.__init__(self,center,cst.YELLOW,surface, board)
        self.blocks.append(block.Block(self.color,center,False,surface, board))
    # Rotate sta

        self.blocks.append(block.Block(self.color,center,False,surface, board))
        center[0]+=1
        self.blocks.append(block.Block(self.color,center,False,surface, board))
        center[1]+=1
        self.blocks.append(block.Block(self.color,center,False,surface, board))
        center[0]-=1
        self.blocks.append(block.Block(self.color,center,False,surface, board))

    # Rotate sta
    
class L1(Form):
    def __init__(self,center,surface, board):
        Form.__init__(self,center,cst.BLUE,surface, board)
        self.blocks.append(block.Block(self.color,center,False,surface, board))
        center[0]+=1
        self.blocks.append(block.Block(self.color,center,False,surface, board))
        center[0]-=2
        self.blocks.append(block.Block(self.color,center,False,surface, board))
        center[1]-=1
        self.blocks.append(block.Block(self.color,center,False,surface, board))

class L2(Form):
    def __init__(self,center,surface, board):
        Form.__init__(self,center,cst.ORANGE,surface, board)
        self.blocks.append(block.Block(self.color,center,False,surface, board))
        center[0]-=1
        self.blocks.append(block.Block(self.color,center,False,surface, board))
        center[0]+=2
        self.blocks.append(block.Block(self.color,center,False,surface, board))
        center[1]-=1
        self.blocks.append(block.Block(self.color,center,False,surface, board))  
        
class Fulger1(Form):
    def __init__(self,center,surface, board):
        Form.__init__(self,center,cst.RED,surface, board)
        self.blocks.append(block.Block(self.color,center,False,surface, board))
        center[0]+=1
        self.blocks.append(block.Block(self.color,center,False,surface, board))
        center[0]-=1
        center[1]-=1
        self.blocks.append(block.Block(self.color,center,False,surface, board))
        center[0]-=1
        self.blocks.append(block.Block(self.color,center,False,surface, board))

class Fulger2(Form):
    def __init__(self,center,surface, board):
        Form.__init__(self,center,cst.GREEN,surface, board)
        self.blocks.append(block.Block(self.color,center,False,surface, board))
        center[0]-=1
        self.blocks.append(block.Block(self.color,center,False,surface, board))
        center[0]+=1
        center[1]-=1
        self.blocks.append(block.Block(self.color,center,False,surface, board))
        center[0]+=1
        self.blocks.append(block.Block(self.color,center,False,surface, board))
  

class Line(Form):
    def __init__(self,center,surface, board):  
        Form.__init__(self,center,cst.CYAN,surface, board)
        self.blocks.append(block.Block(self.color,center,False,surface, board))
        center[0]+=1
        self.blocks.append(block.Block(self.color,center,False,surface, board))
        center[0]+=1
        self.blocks.append(block.Block(self.color,center,False,surface, board))
        center[0]+=1
        self.blocks.append(block.Block(self.color,center,False,surface, board))
