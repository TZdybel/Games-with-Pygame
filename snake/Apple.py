import pygame
import random


class Apple(object):
    def __init__(self, radius, winwidth, winheight, segsize, forbidden):
        self.radius = radius
        self.winwidth = winwidth
        self.winheight = winheight
        self.segsize = segsize
        self.forbidden = forbidden
        self.x = 0
        self.y = 0
        self.setposition()
        self.img = pygame.image.load('imgs/apple.png')

    def setposition(self):
        self.x = random.randrange(self.radius, self.winwidth + 1 - self.radius, self.radius * 2)
        self.y = random.randrange(self.radius + self.segsize, self.winheight + 1 - self.radius - self.segsize, self.radius * 2)
        while (self.x - 10, self.y - 10) in self.forbidden:
            self.x = random.randrange(self.radius, self.winwidth + 1 - self.radius, self.radius * 2)
            self.y = random.randrange(self.radius + self.segsize, self.winheight + 1 - self.radius - self.segsize, self.radius * 2)

    def draw(self, win):
        # pygame.draw.circle(win, (255, 0, 0), (self.x, self.y), self.radius-1)
        win.blit(self.img, (self.x - self.radius, self.y - self.radius - 2))