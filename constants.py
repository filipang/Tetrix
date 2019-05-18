#COLORS
WHITE    = (255,255,255)
RED      = (255,0,0)
GREEN    = (0,255,0)
BLUE     = (0,0,255)
ORANGE   = (255,69,0)
GOLD     = (255,125,0)
YELLOW   = (255,255,0)
PURPLE   = (128,0,128)
CYAN     = (0,255,255) 
BLACK    = (0,0,0)
GRAY     = (100,100,100)

BLOCK_SIZE = 25

BLOCK_WIDTH = 10
BLOCK_HEIGHT = 20

MARGIN = 150

WIDTH = BLOCK_WIDTH*BLOCK_SIZE + 2*MARGIN       +1
HEIGHT = BLOCK_HEIGHT*BLOCK_SIZE                +1

BOARD_WIDTH = BLOCK_WIDTH*BLOCK_SIZE            +1
BOARD_HEIGHT = BLOCK_HEIGHT*BLOCK_SIZE          +1

SIZE = WIDTH,HEIGHT
BOARD_SIZE = BOARD_WIDTH,BOARD_HEIGHT

DISPLAYER_WIDTH=MARGIN
DISPLAYER_HEIGHT=HEIGHT
DISPLAYER_SIZE=DISPLAYER_WIDTH,DISPLAYER_HEIGHT

TIME_MAX=0.7
TIME_ADD=0.2
GRAVITY=True

BOT_PLAY = True