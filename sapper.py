from random import sample
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

    def draw(self):
        color = self.color
        pygame.draw.rect(screen, color,
                         (self.x, self.y,
                          CELL_WIDTH, CELL_WIDTH),
                         width=0)
        pygame.draw.rect(screen, self.color_border,
                         (self.x, self.y,
                          CELL_WIDTH, CELL_WIDTH),
                         width=1)
        if self.opened and not self.bomb and self.near_bombs:
            text = str(self.near_bombs)
            img = pygame.image.load(f'storage/{text}.png')
            img_surf = pygame.transform.scale(img, (55, 55))
            screen.blit(img_surf, (self.x, self.y))

        if self.label:
            flag = pygame.image.load('storage/flag.png')
            flag_surf = pygame.transform.scale(flag, (55, 55))
            screen.blit(flag_surf, (self.x, self.y))


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
    bomb = pygame.image.load('storage/bomb.png')
    bomp_surf = pygame.transform.scale(bomb, (40, 40))
    screen.blit(bomp_surf, (50, y + 5, 40, 40))

    text = "Нажмите любую кнопку "
    follow = FONT20.render(text, True, (0, 0, 0))
    screen.blit(follow, (SIZE[0] - 175, y + 13))

    text = "чтобы начать новую игру"
    follow = FONT20.render(text, True, (0, 0, 0))
    screen.blit(follow, (SIZE[0] - 180, y + 27))

def create_bomb():
    for cell in sample(Cell.cells, k=BOMBS_COUNT):
        cell.bomb = True


def count_labels():
    count = 0
    for cell in Cell.cells:
        if cell.label == "!":
            count += 1
    return count

def main():
    global screen
    screen = pygame.display.set_mode(SIZE)
    pygame.display.set_caption("Sapper")
    clock = pygame.time.Clock()
    create_field()
    while True:
        for cel in Cell.cells:
            cel.draw()
        draw_interface()
        pygame.display.update()
        clock.tick(30)


if __name__ == "__main__":
    main()
