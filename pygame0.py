import pygame, sys
from pygame.locals import *
import random
import math

FPS = 30
fpsClock = pygame.time.Clock()
DISPLAYSURF = pygame.display.set_mode((500, 400), 0, 32)
pygame.display.set_caption('Titel: Animate!')

BLUE  = (0,0,255)
RED = (255,0,0)
GREEN = (0,255,0)
PINK = (255,0,255)
BLACK  = (0,0,0)
WHITE  = (255,255,255)
UP = 'up'
DOWN = 'down'
LEFT = 'left'
RIGHT = 'right'

class Dir:
    def __init__(self):
        self.d = 0
        self.dirs = ['right','down', 'left', 'up']

    def dir(self):
        return self.dirs[self.d]

    def nextDir(self):
        self.d = (self.d + 1)%4

class Square:
    def __init__(self, surface):
        self.x = int(math.floor(random.random()*398)+51)
        self.y = int(math.floor(random.random()*99)+300)
        self.surface = surface
        self.color = BLUE

    def move(self, dir=None):
        if dir is UP:
            self.y -= 10
        if dir is DOWN:
            self.y += 10
        if dir is LEFT:
            self.x -= 8
        if dir is RIGHT:
            self.x += 8

    def get(self):
        return {'x': self.x, 'y': self.y}

    def col(self, c):
        self.color = c

    def draw(self):
         pygame.draw.rect(self.surface, self.color, (self.x, self.y, 20, 20))

direction = 'left'
d = Dir()
c = Square(DISPLAYSURF)
cMovingLeft = False
cMovingRight= False
cMovingDown= False
cJumping= False

def terminate():
    pygame.quit()
    sys.exit()

while True:
    DISPLAYSURF.fill(WHITE)
    c.draw()

    for event in pygame.event.get():
        if event.type == QUIT:
            terminate()
        elif event.type == KEYDOWN:
            if event.key == K_a:
                c.move(LEFT)
                cMovingLeft = True
            if event.key == K_d:
                c.move (RIGHT)
                cMovingRight = True
            if event.key == K_w and cJumping == False and cMovingDown == False:
                cJumping = True
            if event.key == K_ESCAPE:
                terminate()
        elif event.type == KEYUP:
            if event.key == K_a:
                cMovingLeft = False
                c.col(BLUE)
            if event.key == K_d:
                cMovingRight = False
                c.col(BLUE)

    if cMovingLeft == True:
        c.move(LEFT)
        c.col(RED)
    if cMovingRight == True:
        c.move(RIGHT)
        c.col(GREEN)
    if cMovingDown == True:
        c.move(DOWN)
    if cJumping == True:
        c.col(PINK)
        c.move(UP)
    if c.get()['y'] <= 350:
        cJumping = False
        c.col(BLUE)
        cMovingDown = True
    if c.get()['y'] >= 379:
        cMovingDown = False

    pygame.display.update()
    fpsClock.tick(FPS)
