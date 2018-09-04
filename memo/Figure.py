import pygame
import random


class Figure(object):
    shapes = ['rect', 'circle', 'diamond', 'triangle', 'ring']
    colors = [(255, 255, 255), (255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (0, 255, 255), (255, 0, 255),
              (200, 200, 200), (255, 0, 100), (0, 255, 100), (100, 0, 255), (100, 255, 0), (0, 100, 255), (255, 100, 0)]
    border = 10

    def __init__(self, color, shape):
        self.color = color
        self.shape = shape
        self.covered = True

    @staticmethod
    def createpair():
        color = Figure.colors[random.randrange(len(Figure.colors))]
        shape = Figure.shapes[random.randrange(len(Figure.shapes))]
        return Figure(color, shape), Figure(color, shape)

    def draw(self, win, x, y, segsize):
        if self.shape == 'rect':
            self.drawrect(win, x, y, segsize)
        elif self.shape == 'circle':
            self.drawcircle(win, x, y, segsize)
        elif self.shape == 'diamond':
            self.drawdiamond(win, x, y, segsize)
        elif self.shape == 'triangle':
            self.drawtriangle(win, x, y, segsize)
        else:
            self.drawring(win, x, y, segsize)

    def drawcircle(self, win, x, y, segsize):
        radius = segsize//2
        x += radius
        y += radius
        pygame.draw.circle(win, self.color, (x, y), radius - self.border)

    def drawrect(self, win, x, y, segsize):
        pygame.draw.rect(win, self.color, (x + self.border, y + self.border, segsize - 2*self.border, segsize - 2*self.border))

    def drawdiamond(self, win, x, y, segsize):
        pygame.draw.polygon(win, self.color, [(x + segsize//2, y + self.border), (x + segsize - self.border, y + segsize//2),
                                              (x + segsize//2, y + segsize - self.border), (x + self.border, y + segsize//2)])

    def drawtriangle(self, win, x, y, segsize):
        pygame.draw.polygon(win, self.color, [(x + self.border, y + self.border), (x + segsize - self.border, y + self.border),
                                              (x + segsize//2, y + segsize - self.border)])

    def drawring(self, win, x, y, segsize):
        radius = segsize//2
        x += radius
        y += radius
        pygame.draw.circle(win, self.color, (x, y), radius - self.border)
        pygame.draw.circle(win, (0, 0, 0), (x, y), radius - self.border - radius//2)

    def __eq__(self, other):
        if isinstance(other, int): return False
        return self.color == other.color and self.shape == other.shape
