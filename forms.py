import block
import pygame
import constants as cst

class Form:
    def __init__(self,center,color,surface):
        self.center=center
        self.surface=surface
        self.color=color
        self.blocks=[]     
    def rotate(self):
        return
    def down(self,nr=1):
        #print(len(self.blocks))
        #for b in self.blocks:
            
        for b in self.blocks:
            pygame.draw.rect(b.surface, cst.BLACK, b.rect)
        for b in self.blocks:
            
            b.down(nr,False)

    def left(self,nr=1):
        #print(len(self.blocks))
        for b in self.blocks:
            pygame.draw.rect(b.surface, cst.BLACK, b.rect)
        for b in self.blocks:
            b.left(nr,False)

    def right(self,nr=1):
        #print(len(self.blocks))
        for b in self.blocks:
            pygame.draw.rect(b.surface, cst.BLACK, b.rect)
        for b in self.blocks:
            b.right(nr,False)

class Square(Form):
    def __init__(self,center,surface):
        Form.__init__(self,center,cst.YELLOW,surface)
        self.blocks.append(block.Block(self.color,center,False,surface))
    # Rotate sta

        self.blocks.append(block.Block(self.color,center,False,surface))
        center[0]+=1
        self.blocks.append(block.Block(self.color,center,False,surface))
        center[1]+=1
        self.blocks.append(block.Block(self.color,center,False,surface))
        center[0]-=1
        self.blocks.append(block.Block(self.color,center,False,surface))
    # Rotate sta
    
class L1(Form):
    def __init__(self,center,surface):
        Form.__init__(self,center,cst.BLUE,surface)
        self.blocks.append(block.Block(self.color,center,False,surface))
        center[0]+=1
        self.blocks.append(block.Block(self.color,center,False,surface))
        center[0]-=2
        self.blocks.append(block.Block(self.color,center,False,surface))
        center[1]-=1
        self.blocks.append(block.Block(self.color,center,False,surface))

class L2(Form):
    def __init__(self,center,surface):
        Form.__init__(self,center,cst.ORANGE,surface)
        self.blocks.append(block.Block(self.color,center,False,surface))
        center[0]-=1
        self.blocks.append(block.Block(self.color,center,False,surface))
        center[0]+=2
        self.blocks.append(block.Block(self.color,center,False,surface))
        center[1]-=1
        self.blocks.append(block.Block(self.color,center,False,surface))  
        
class Fulger1(Form):
    def __init__(self,center,surface):
        Form.__init__(self,center,cst.RED,surface)
        self.blocks.append(block.Block(self.color,center,False,surface))
        center[0]+=1
        self.blocks.append(block.Block(self.color,center,False,surface))
        center[0]-=1
        center[1]-=1
        self.blocks.append(block.Block(self.color,center,False,surface))
        center[0]-=1
        self.blocks.append(block.Block(self.color,center,False,surface))

class Fulger2(Form):
    def __init__(self,center,surface):
        Form.__init__(self,center,cst.GREEN,surface)
        self.blocks.append(block.Block(self.color,center,False,surface))
        center[0]-=1
        self.blocks.append(block.Block(self.color,center,False,surface))
        center[0]+=1
        center[1]-=1
        self.blocks.append(block.Block(self.color,center,False,surface))
        center[0]+=1
        self.blocks.append(block.Block(self.color,center,False,surface))
  

class Line(Form):
    def __init__(self,center,surface):  
        Form.__init__(self,center,cst.CYAN,surface)
        self.blocks.append(block.Block(self.color,center,False,surface))
        center[0]+=1
        self.blocks.append(block.Block(self.color,center,False,surface))
        center[0]+=1
        self.blocks.append(block.Block(self.color,center,False,surface))
        center[0]+=1
        self.blocks.append(block.Block(self.color,center,False,surface))


if("__main__"==__name__):## Test ONLY
    s=Square([33,33],[200,200,200],22)
    s.rotate()
    print(s)