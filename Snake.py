import pygame


class Snake(object):
    def __init__(self, x, y, vel, segwidth, segheigth):
        self.x = x
        self.y = y
        self.vel = vel
        self.segments = [(x, y), (x - segwidth - 5, y), (x - 2 * segwidth - 5, y)]
        self.segwidth = segwidth
        self.segheigth = segheigth
        self.direction = (0, 1)
        self.head = pygame.image.load('imgs/snake.png')

    def move(self):
        self.segments.insert(0, (self.x, self.y))
        self.segments.pop()

    def draw(self, win):
        if self.direction[0] != -1:
            rothead = pygame.transform.rotate(self.head, self.direction[0]*(-180)+self.direction[1]*(-90))
        else:
            rothead = self.head
        win.blit(rothead, (self.segments[0][0], self.segments[0][1]))
        for seg in self.segments[1:]:
            pygame.draw.rect(win, (0, 255, 0), (seg[0], seg[1], self.segwidth, self.segheigth))

    def addsegment(self):
        self.segments.append(self.segments[-1])