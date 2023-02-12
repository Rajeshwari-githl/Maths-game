import pygame, sys, time, random, math
from pygame.locals import *

BACKGROUNDCOLOR = (255, 255, 255)

WINDOWW = 800 
WINDOWH = 600
PLAYERW = 66
PLAYERH = 22
FPS = 60
MOVESPEED = 3
YACCEL = 0.13
GRAVITY = 2
BLOCKSIZE = 30

pygame.init()
screen = pygame.display.set_mode((WINDOWW, WINDOWH), 0, 32)
mainClock = pygame.time.Clock()

testLevel = [
            (1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,),
            (1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,),
            (1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,),
            (1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,),
            (1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,),
            (1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,),
            (1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,),
            (1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,),
            (1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,),
            (1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,),
            (1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,),
            (1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,),
            (1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,0,0,0,0,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,),
            (1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,),
            (1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,),
            (1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,0,0,0,0,0,0,0,0,),
            (1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,),
            (1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,),
            (1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,),
            (1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,)]

def createblock(length, height, color):
    tmpblock = pygame.Surface((length, height))
    tmpblock.fill(color)
    tmpblock.convert()
    return tmpblock

def terminate(): # Used to shut down the software
    pygame.quit()
    sys.exit()

def add_level(lvl, bSize): # Creates the level based on a map (lvl) and the size of blocks
    bList = [] # List of every block
    bListDisp = [] # List of every block to display    
    bTypeList = [] # List with corresponding type of block(wall, air, etc.)

    for y in range(len(lvl)): 
        for x in range(len(lvl[0])):

            if lvl[y][x] == 0: # If the block type on lvl[y][x] is '0', write "air" down in the type list
                bTypeList.append("air")
            elif lvl[y][x] == 1: # If the block type on lvl[y][x] is '1', write "wall" down in the type list
                bTypeList.append("solid")

            bList.append(pygame.Rect((bSize * x), (bSize * y), bSize, bSize)) #Append every block that is registered
            bListDisp.append(pygame.Rect((bSize * x), (bSize * y), bSize, bSize)) #Append every block to display that is registered

    return bList, bListDisp, bTypeList

player = pygame.Rect((WINDOWW/2), (WINDOWH - BLOCKSIZE*3), PLAYERW, PLAYERH)
wallblock = createblock(BLOCKSIZE, BLOCKSIZE,(20,0,50))

lastTime = pygame.time.get_ticks()
isGrounded = False

vx = 0
vy = 0

allLevels = [testLevel] # A list containing all lvls(only one for now)
maxLevel = len(allLevels) # Checks which level is the last
currLevel = allLevels[0] # Current level(start with the first lvl)
blockList, blockListDisp, blockTypeList = add_level(currLevel, BLOCKSIZE) # A list with every block and another list with the blocks types

thrusters = True
jumping = False
falling = True
while True:
    """COLLISION"""
    collision = False
    for i in range(len(blockTypeList)):
        if blockTypeList[i] == "solid":
            if player.colliderect(blockList[i]): 
                collision = True
                if vx > 0 and not falling:
                    player.right = blockListDisp[i].left
                    vx = 0
                    print('Collide Right')
                if vx < 0 and not falling:
                    player.left = blockListDisp[i].right
                    vx = 0
                    print('Collide Left')
                if vy > 0:
                    player.bottom = blockListDisp[i].top
                    isGrounded = True
                    falling = False
                    vy = 0
                    print('Collide Bottom')
                if vy < 0:
                    player.top = blockListDisp[i].bottom
                    vy = 0
                    print('Collide Top')
            else:
                player.bottom += 1
                if player.colliderect(blockList[i]):
                    collision = True
                    #isGrounded = True
                    #falling = False
                player.bottom -= 1
    if not collision:
        falling = True
        isGrounded = False

    # Input
    pressedKeys = pygame.key.get_pressed() # Checks which keys are being pressed
    timeDiff = pygame.time.get_ticks() - lastTime # Calculates time difference 
    lastTime +=  timeDiff # Last time checked reset to current time

    # Shut-down if the ESC-key is pressed or the window is "crossed down"
    for event in pygame.event.get():
        if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
            terminate()    

    """X-axis control"""
    if pressedKeys[ord('a')]:
        vx = -MOVESPEED
    if pressedKeys[ord('d')]:
        vx = MOVESPEED
    if not pressedKeys[ord('d')] and not pressedKeys[ord('a')]:
        vx = 0

    """Y-axis control"""
    # Controls for jumping
    if pressedKeys[ord('w')] and thrusters == True:
            vy -= YACCEL * timeDiff; # Accelerate along the y-xis when "jumping", but not above/below max speed
            if vy <= -4:
                vy = -4
            isGrounded = False # You are airborne
            jumping = True # You are jumping

    if event.type == KEYUP: # If you let go of the "jump"-button, stop jumping
        if event.key == ord('w') and vy < 0 and not isGrounded:
            jumping = False
            falling = True

    player.x += vx
    player.y += vy

    # Gravity
    if not isGrounded or falling:
        vy += 0.3
        if vy > 80:
            vy = 80

    screen.fill(BACKGROUNDCOLOR)

    for i in range(len(blockTypeList)):
        if blockTypeList[i] == "solid":
            screen.blit(wallblock, (blockListDisp[i].x, blockListDisp[i].y)) #blit the wall-block graphics

    pygame.draw.rect(screen, (0, 0, 0), player)

    pygame.display.update()
    mainClock.tick(FPS)