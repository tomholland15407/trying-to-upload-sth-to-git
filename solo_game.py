import pygame
import random

pygame.init()
WIDTH = 1000
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Catch the egg")
CELL_SIZE = 20

WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
BROWN = (106, 51, 51)

clock = pygame.time.Clock()
FPS = 1

rect = pygame.Rect(470, 580, CELL_SIZE*3, CELL_SIZE)

class Egg:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = CELL_SIZE
        self.height = CELL_SIZE
        self.drop_rate = random.uniform(0.01, 0.1)
    def draw(self, surface):
        pygame.draw.rect(surface, WHITE, (self.x, self.y, self.width, self.height))
    def egg_drop(self):
        self.y += self.drop_rate

eggs = []

running = True

while running:
    screen.fill(GREEN)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            x = random.randint(0, 980)
            eggs.append(Egg(x,0))
    for egg in eggs:
        egg.draw(screen)
        egg.egg_drop()


    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        rect.x += 1
    if keys[pygame.K_LEFT]:
        rect.x -= 1

    pygame.draw.rect(screen, BROWN, rect)

    pygame.display.flip()

pygame.quit()



