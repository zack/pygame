import pygame, sys
from pygame.locals import *
import random
import math

FPS = 30
fpsClock = pygame.time.Clock()
DISPLAYSURF = pygame.display.set_mode((500, 400), 0, 32)
pygame.display.set_caption('Titel: Animate!')

BLUE  = (0,0,255)
BLACK  = (0,0,0)

class Dir:
    def __init__(self):
        self.d = 0
        self.dirs = ['right','down', 'left', 'up']

    def dir(self):
        return self.dirs[self.d]

    def nextDir(self):
        self.d = (self.d + 1)%4

class Circle:
    def __init__(self, surface):
        self.x = int(math.floor(random.random()*500))
        self.y = int(math.floor(random.random()*400))
        self.surface = surface

    def set(self, x=None, y=None, ax=None, ay=None):
        if x is not None:
            self.x = x
        if y is not None:
            self.y = y
        if ax is not None:
            self.x += ax
        if ay is not None:
            self.y += ay

    def get(self):
        return {'x': self.x, 'y': self.y}

    def draw(self):
         pygame.draw.circle(self.surface, BLUE, (self.x, self.y), 20, 0)

direction = 'left'
d = Dir()
c = Circle(DISPLAYSURF)

while True:
        DISPLAYSURF.fill(BLACK)
	if d.dir() == 'right':
		c.set(ax=10)
		if c.get()['x'] >= 450:
			d.nextDir()
	if d.dir() == 'down':
		c.set(ay=10)
		if c.get()['y'] >= 350:
			d.nextDir()
	if d.dir() == 'left':
		c.set(ax=-10)
		if c.get()['x'] <= 50:
			d.nextDir()
	if d.dir() == 'up':
		c.set(ay=-10)
		if c.get()['y'] <= 50:
			d.nextDir()

        c.draw()

	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()

	pygame.display.update()
        fpsClock.tick(FPS)
