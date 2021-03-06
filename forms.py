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

    def checkLost(self):
        for b in self.blocks:
            if b.coords[1]<1 or self.board[b.coords[0]][b.coords[1]]!=None:
                return True
        return False
    
    def moveWith(self,x,y,f=True,draw=True):
        if(f):
            for b in self.blocks:
                if not b.can(b.coords[0]+x,b.coords[1]+y):
                    return False
        if draw:
            if(f):
                self.delete()
            else:
                self.delete(cst.GRAY)
        for b in self.blocks:
            b.moveWith(x,y,False,draw)
        self.center[0]+=x
        self.center[1]+=y
        return True
    
    def delete(self,color=cst.BLACK):
        for b in self.blocks:
            b.delete(color)
    
    def rotate(self,offset_x = 0, offset_y = 0,draw = True): #clock-wise rotation

        for b in self.blocks:
            x = b.coords[0]
            y = b.coords[1]
            center_x = self.center[0]
            center_y = self.center[1]
            x = x - center_x
            y = y - center_y
            new_x = center_x - y + offset_x
            new_y = center_y + x + offset_y
            if not(b.can(new_x,new_y)):
                if offset_x==0 and offset_y==0:
                    offx=[1,-1,0,0,-2,2,1,1,0,0,-1,-1,-1,1,-1,-2,1,2,-2,2]
                    offy=[0,0,1,-1,0,0,1,-1,2,-2,1,-1,2,-2,-2,1,2,-1,-1,1]
                    for i in range(len(offx)):
                        if(self.rotate(offx[i],offy[i],draw)):
                            return True

                    return False
                else:
                    return False

        if draw:
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

                b.move(center_x-y+offset_x,center_y+x+offset_y,False,draw)

        self.center[0]+=offset_x
        self.center[1]+=offset_y

        return True
    
    def lock(self):
        if self.checkLost():
            return False
        
        for b in self.blocks:
            self.board[b.coords[0]] [b.coords[1]] = b
            self.board[0][b.coords[1]]+=1
        return True


class Square(Form):
    def __init__(self,center,surface, board):
        Form.__init__(self,center,cst.YELLOW,surface, board)
        self.blocks.append(block.Block(self.color,center,False,surface, board))
        center[0]-=1
        self.blocks.append(block.Block(self.color,center,False,surface, board))
        center[1]-=1
        self.blocks.append(block.Block(self.color,center,False,surface, board))
        center[0]+=1
        self.blocks.append(block.Block(self.color,center,False,surface, board))

    def rotate(self,aux1=None,aux2=None,aux3=None):
        return
    
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
        center[0]-=3
        self.blocks.append(block.Block(self.color,center,False,surface, board))
        
class T(Form):
    def __init__(self,center,surface, board):  
        Form.__init__(self,center,cst.PURPLE,surface, board)
        self.blocks.append(block.Block(self.color,center,False,surface, board))
        center[0]-=1;
        self.blocks.append(block.Block(self.color,center,False,surface, board))
        center[0]+=2;
        self.blocks.append(block.Block(self.color,center,False,surface, board))
        center[0]-=1;
        center[1]-=1;
        self.blocks.append(block.Block(self.color,center,False,surface, board))

