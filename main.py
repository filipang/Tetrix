import Game
import pygame
import sys
import time


def exit():
    #print("BYE") #debug
    pygame.quit()
    sys.exit()

class Main:
    def __init__(self):
        pygame.init()
        self.Game=Game.Tetris()
    def Start(self):
        self.Game.start()
    def Wait(self):
        try:
            #print("IN")
            while self.Game.ON:
               pygame.event.pump()
            #print("EXIT")
        except KeyboardInterrupt:
            None
            
        self.Game.ON=False
        print("Score:",self.Game.Levels)
        time.sleep(0.000000001)
    
if(__name__=="__main__"):        
    M=Main()
    M.Start()
    M.Wait()
    exit()
