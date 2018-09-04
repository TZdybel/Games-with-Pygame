import pygame, os, random, datetime
from Figure import Figure

os.environ['SDL_VIDEO_CENTERED'] = '1'

pygame.init()
pygame.display.set_caption("Memo")

font = pygame.font.SysFont("pepperoni pizza", 100)
font2 = pygame.font.SysFont("arial", 25)

panel = 40
winwidth = 800
winheigth = 400
win = pygame.display.set_mode((winwidth, panel + winheigth))

segsize = 100
segnumber = (winwidth//segsize) * (winheigth//segsize)

positions = []
board = random.sample(range(1, segnumber+1), segnumber)
colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (255, 0, 255), (0, 255, 255)]

clock = pygame.time.Clock()
FPS = 30


def init():
    for x in range(0, winwidth // segsize):
        for y in range(0, winheigth // segsize):
            positions.append((x * segsize, panel + y * segsize))

    for i in range(1, segnumber, 2):
        f1, f2 = Figure.createpair()
        board.insert(board.index(i), f1)
        board.remove(i)
        board.insert(board.index(i + 1), f2)
        board.remove(i + 1)


def drawboard():
    win.fill((0, 0, 0))

    seconds = (pygame.time.get_ticks()-startticks)//1000
    time = str(datetime.timedelta(seconds=seconds))
    time = font2.render(time, 1, (255, 255, 255))
    win.blit(time, (winwidth//2 - 40, 7))

    for i in range(segnumber):
        if not board[i].covered:
            board[i].draw(win, positions[i][0], positions[i][1], segsize)
        else:
            pygame.draw.rect(win, (100, 100, 100), (positions[i][0] + 2, positions[i][1] + 2, segsize - 4, segsize - 4))
    pygame.display.update()


def main():
    global startticks

    init()
    guessing = False
    comparefig = None
    running = True
    won = False

    startticks = pygame.time.get_ticks()

    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if not won:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    for i, el in enumerate(positions):
                        if el[0] <= pos[0] <= el[0] + segsize and el[1] <= pos[1] <= el[1] + segsize:
                            if board[i].covered:
                                board[i].covered = False
                                if guessing:
                                    if board[i] != comparefig:
                                        drawboard()
                                        pygame.time.delay(500)
                                        board[i].covered = True
                                        comparefig.covered = True
                                    guessing = False
                                else:
                                    guessing = True
                                    comparefig = board[i]
            else:
                if event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.KEYDOWN:
                    running = False

        if won:
            victory = font.render("VICTORY!", 1, colors[random.randrange(len(colors))])
            win.blit(victory, (winwidth // 2 - 300, winheigth // 2 - 50))
            pygame.display.update()
            pygame.time.delay(200)
            continue
        drawboard()

        counter = 0
        for el in board:
            if not el.covered:
                counter += 1

        if counter == segnumber:
            won = True

    pygame.quit()


if __name__ == '__main__':
    main()