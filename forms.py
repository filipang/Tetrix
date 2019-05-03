import block

class Form:
    def __init__(self,center,color,surface):
        self.center=center
        self.surface=surface
        self.color=color
        self.blocks=[]     
    def rotate(self):
        return

class Square(Form):
    def __init__(self,center,color,surface):
        Form.__init__(self,center,color,surface)
        #self.blocks.append(Block(color,center,False,surface))
    # Rotate sta
    
if("__main__"==__name__):## Test ONLY
    s=Square([33,33],[200,200,200],22)
    s.rotate()
    print(s)