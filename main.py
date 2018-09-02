import pygame
import Snake, Apple
import os

os.environ['SDL_VIDEO_CENTERED'] = '1'

pygame.mixer.pre_init(44100, -16, 1, 512)
pygame.init()
pygame.display.set_caption("Sssssnake")

# 10x10 segments
winwidth = 200
winheight = 240
win = pygame.display.set_mode((winwidth, winheight))

# segment - 20x20px
segsize = 20
snake = Snake.Snake(0, 20, segsize, segsize-2, segsize-2)
apple = Apple.Apple(segsize//2, winwidth, winheight, segsize, snake.segments)

# font
font = pygame.font.SysFont("monospace", 15)

# sounds
eatsound = pygame.mixer.Sound('sounds/eat sound.wav')
losesound = pygame.mixer.Sound('sounds/lose sound.wav')
music = pygame.mixer.music.load('sounds/bg music.mp3')
pygame.mixer.music.play(-1)


def lost():
    pygame.mixer.music.stop()
    losesound.play()
    global win, running, snake, score
    gameover = font.render("GAME OVER :(", 1, (255, 255, 255))
    playagain = font.render("Play again?", 1, (255, 255, 255))
    yorn = font.render("(y)   (n)", 1, (255, 255, 255))
    win.blit(gameover, (winwidth//2 - 55, winheight//2 - 35))
    win.blit(playagain, (winwidth//2 - 52, winheight//2 - 15))
    win.blit(yorn, (winwidth//2 - 40, winheight//2))
    pygame.display.update()
    pygame.event.clear()
    while True:
        event = pygame.event.wait()
        if event.type == pygame.QUIT:
            running = False
            break
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_y:
                snake = Snake.Snake(0, 20, segsize, segsize-2, segsize-2)
                apple.forbidden = snake.segments
                score = 0
                pygame.mixer.music.play(-1)
                break
            if event.key == pygame.K_n:
                running = False
                break


# mainloop
running = True
score = 0
while running:
    pygame.time.delay(200)
    keypressed = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and not keypressed:
            if event.key == pygame.K_UP and snake.direction != (1, 0):
                snake.direction = (-1, 0)
                keypressed = True
            elif event.key == pygame.K_DOWN and snake.direction != (-1, 0):
                snake.direction = (1, 0)
                keypressed = True
            elif event.key == pygame.K_LEFT and snake.direction != (0, 1):
                snake.direction = (0, -1)
                keypressed = True
            elif event.key == pygame.K_RIGHT and snake.direction != (0, -1):
                snake.direction = (0, 1)
                keypressed = True

    # calculating new position
    tempx = snake.x + snake.vel * snake.direction[1]
    tempy = snake.y + snake.vel * snake.direction[0]
    if 0 <= tempx <= winwidth - snake.segwidth and segsize <= tempy <= winheight - segsize - snake.segheigth:
        snake.x = tempx
        snake.y = tempy
    else:
        #collision with borders
        lost()
        continue

    snake.move()

    # collision with snake
    if snake.segments.count((snake.x, snake.y)) > 1:
        lost()
        continue

    win.fill((0, 0, 0))
    # collision with apple
    if snake.x <= apple.x <= snake.x + segsize and snake.y <= apple.y <= snake.y + segsize:
        eatsound.play()
        snake.addsegment()
        snake.draw(win)
        apple.setposition()
        score += 1
    else:
        snake.draw(win)

    label = font.render("Score {}".format(score), 1, (255, 255, 255))
    win.blit(label, (winwidth - 70, 0))
    apple.draw(win)
    pygame.draw.rect(win, (255, 255, 0), (1, 20, winwidth - 2, winheight - 2*segsize), 1)
    pygame.display.update()

pygame.quit()