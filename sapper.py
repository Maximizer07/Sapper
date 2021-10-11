import pygame

pygame.init()

SIZE = 600, 650
CELL_WIDTH = 60
BOMBS_COUNT = 10
FONT50 = pygame.font.SysFont("microsofttalie", 50)
FONT20 = pygame.font.SysFont("microsofttalie", 20)


class Cell:
    cells = []

    def __init__(self, x, y, bomb=False):
        self.x = x
        self.y = y
        self.bomb = bomb
        self.color = (179, 179, 179)
        self.color_border = (122, 122, 122)
        self.near_bombs = 0
        self.opened = False
        self.label = None

        self.cells.append(self)


def create_field():
    Cell.cells = []
    for x in range(0, SIZE[0], CELL_WIDTH):
        for y in range(0, SIZE[1] - 50, CELL_WIDTH):
            Cell(x, y)
    return Cell


def draw_interface():
    y = SIZE[1] - 50
    pygame.draw.rect(screen, (255, 255, 255),
                     (0, y, SIZE[0], 50),
                     width=0)


def main():
    global screen
    screen = pygame.display.set_mode(SIZE)
    pygame.display.set_caption("Sapper")
    clock = pygame.time.Clock()
    create_field()
    while True:
        draw_interface()
        pygame.display.update()
        clock.tick(30)


if __name__ == "__main__":
    main()
