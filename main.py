import Game
import pygame
import sys
import time


def exit():
    #print("BYE") #debug
    pygame.quit()
    sys.exit()

class Main_Thread:
    def __init__(self):
        pygame.init()
        self.Game=Game.Tetris()
    def Start(self):
        self.Game.start()
    def Wait(self):
        try:
            #print("IN")
            while self.Game.ON:
                None
            #print("EXIT")
        except KeyboardInterrupt:
            None
            
        self.Game.ON=False
        print("Score:",self.Game.Levels)
        time.sleep(0.000000001)

class Main_NoThread:
    def __init__(self):
        pygame.init()
        self.Game=Game.Tetris()
    def Start(self):
        self.Game.run()
    def Wait(self):
        try:
            #print("IN")
            while self.Game.ON:
                self.Game.run()
            #print("EXIT")
        except KeyboardInterrupt:
            None
            
        self.Game.ON=False
        print("Score:",self.Game.Levels)
        time.sleep(0.000000001)
    
if(__name__=="__main__"):        
    M=Main_NoThread()
    M.Start()
    M.Wait()
    exit()
